<?php
declare(strict_types=1);

/**
 * 長期インターン エントリーフォーム 受信ハンドラ
 * eXs (exs-mobi) の contact_submit.php / partner-entry.php を参考に作成。
 * SMTP 設定 (intern-entry-config.local.php) があれば PHPMailer、
 * なければ mb_send_mail にフォールバックする。
 */

header('X-Frame-Options: SAMEORIGIN');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') {
    header('Location: index.html#entry');
    exit;
}

mb_internal_encoding('UTF-8');

function posted(string $key): string
{
    return trim((string)($_POST[$key] ?? ''));
}

function allowOriginOrReferer(array $allowedHosts): bool
{
    $check = static function (string $url) use ($allowedHosts): bool {
        if ($url === '') {
            return true; // 送られてこない環境もあるため許容
        }
        $host = strtolower((string)parse_url($url, PHP_URL_HOST));
        return $host !== '' && in_array($host, $allowedHosts, true);
    };
    return $check(trim((string)($_SERVER['HTTP_ORIGIN'] ?? '')))
        && $check(trim((string)($_SERVER['HTTP_REFERER'] ?? '')));
}

/* ---- 入力取得 ---- */
$position  = posted('position');
$start     = posted('start');
$name      = posted('name');
$kana      = posted('kana');
$email     = posted('email');
$tel       = posted('tel');
$school    = posted('school');
$faculty   = posted('faculty');
$grade     = posted('grade');
$grad      = posted('grad');
$area      = posted('area');
$portfolio = posted('portfolio');
$interest  = posted('interest');
$message   = posted('message');
$privacy   = posted('privacy');

/* ---- スパム対策フィールド ---- */
$honeypot      = posted('company_hp');   // 人間には見えない。値が入っていたらボット。
$jsEnabled     = posted('js_enabled');   // JS で 1 に書き換わる
$csrfToken     = posted('csrf_token');   // JS が付与
$formStartedAt = (int)posted('form_started_at');

/* ---- バリデーション ---- */
$errors = [];
$now = time();

$allowedPositions = ['企画・マーケティング', 'クリエイティブ制作', 'まだ決めていない・相談したい'];

if (!in_array($position, $allowedPositions, true)) {
    $errors[] = 'position';
}
if ($name === '' || mb_strlen($name) > 80 || preg_match('/[\r\n]/', $name)) {
    $errors[] = 'name';
}
if ($kana === '' || mb_strlen($kana) > 80 || preg_match('/[\r\n]/', $kana)) {
    $errors[] = 'kana';
}
if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || mb_strlen($email) > 255 || preg_match('/[\r\n]/', $email)) {
    $errors[] = 'email';
}
if ($tel === '' || !preg_match('/^[0-9+\-() ]{6,30}$/', $tel)) {
    $errors[] = 'tel';
}
if ($school === '' || mb_strlen($school) > 120 || preg_match('/[\r\n]/', $school)) {
    $errors[] = 'school';
}
// 区分により必須項目を変える
$inSchool = in_array($grade, ['学部1年', '学部2年', '学部3年', '学部4年', '修士1年', '修士2年', '海外大学', '短大', '専門学校生', '高専'], true);
$facultyRequired = $inSchool || in_array($grade, ['既卒', '第二新卒'], true);
if (mb_strlen($faculty) > 120 || preg_match('/[\r\n]/', $faculty)) {
    $errors[] = 'faculty';
} elseif ($facultyRequired && $faculty === '') {
    $errors[] = 'faculty';
}
if ($grade === '' || mb_strlen($grade) > 40) {
    $errors[] = 'grade';
}
// 在学中は卒業予定年月を必須に
if ($inSchool && $grad === '') {
    $errors[] = 'grad';
}
if (mb_strlen($interest) > 2000 || mb_strlen($message) > 3000) {
    $errors[] = 'length';
}
if ($privacy !== '1') {
    $errors[] = 'privacy';
}

/* ---- ボット・不正送信対策 ---- */
$allowedHosts = ['customjapan.jp', 'www.customjapan.jp'];
$requestHost = strtolower((string)($_SERVER['HTTP_HOST'] ?? ''));
if ($requestHost !== '') {
    $allowedHosts[] = $requestHost;
}
$allowedHosts = array_values(array_unique($allowedHosts));

if ($honeypot !== '') {
    $errors[] = 'honeypot';
}
if ($jsEnabled !== '1') {
    $errors[] = 'js';
}
if ($csrfToken === '') {
    $errors[] = 'csrf';
}
if (!allowOriginOrReferer($allowedHosts)) {
    $errors[] = 'origin';
}
// フォーム表示から 1 秒未満 / 2 時間超は不正・期限切れ扱い
if ($formStartedAt <= 0 || ($now - $formStartedAt) < 1 || ($now - $formStartedAt) > 7200) {
    $errors[] = 'time';
}

if (!empty($errors)) {
    header('Location: intern-error.html?form=intern');
    exit;
}

/* ---- メール本文 ---- */
$ip = (string)($_SERVER['REMOTE_ADDR'] ?? 'unknown');
$ua = substr((string)($_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 180);

$subject = '【カスタムジャパン】長期インターン エントリー';
$body = implode("\n", [
    '長期インターン エントリーフォームから応募がありました。',
    '',
    '希望職種: ' . $position,
    '勤務開始時期: ' . ($start !== '' ? $start : '未定'),
    'お名前: ' . $name,
    'フリガナ: ' . $kana,
    'メールアドレス: ' . $email,
    '電話番号: ' . $tel,
    '学校名: ' . $school,
    '学部・学科: ' . $faculty,
    '学年: ' . $grade,
    '卒業予定: ' . ($grad !== '' ? $grad : '未定'),
    'お住まい: ' . ($area !== '' ? $area : '-'),
    'ポートフォリオ/SNS: ' . ($portfolio !== '' ? $portfolio : '-'),
    '',
    '興味のある領域:',
    ($interest !== '' ? $interest : '-'),
    '',
    '志望動機・自己PR:',
    ($message !== '' ? $message : '-'),
    '',
    '---',
    '送信元IP: ' . $ip,
    'UA: ' . $ua,
    'Referer: ' . (string)($_SERVER['HTTP_REFERER'] ?? '-'),
]);

/* ---- 設定ロード (任意) ---- */
$config = [];
$configPath = __DIR__ . '/intern-entry-config.local.php';
if (file_exists($configPath)) {
    $loaded = require $configPath;
    if (is_array($loaded)) {
        $config = $loaded;
    }
}
$toList = (isset($config['to']) && is_array($config['to']) && !empty($config['to']))
    ? $config['to']
    : ['recruit@customjapan.jp'];
$ccList   = (isset($config['cc']) && is_array($config['cc'])) ? $config['cc'] : [];
$from     = (string)($config['from'] ?? 'noreply@customjapan.jp');
$fromName = (string)($config['from_name'] ?? 'CUSTOM JAPAN Internship');

/* ---- PHPMailer 準備 (あれば) ---- */
$phpMailerReady = false;
if (file_exists(__DIR__ . '/vendor/autoload.php')) {
    require_once __DIR__ . '/vendor/autoload.php';
    $phpMailerReady = class_exists('\\PHPMailer\\PHPMailer\\PHPMailer');
} elseif (file_exists(__DIR__ . '/_PhP_Mailer_/src/PHPMailer.php')) {
    require_once __DIR__ . '/_PhP_Mailer_/src/Exception.php';
    require_once __DIR__ . '/_PhP_Mailer_/src/PHPMailer.php';
    require_once __DIR__ . '/_PhP_Mailer_/src/SMTP.php';
    $phpMailerReady = class_exists('\\PHPMailer\\PHPMailer\\PHPMailer');
}

$smtp = isset($config['smtp']) && is_array($config['smtp']) ? $config['smtp'] : [];
$useSmtp = $phpMailerReady
    && !empty($smtp['host']) && !empty($smtp['username']) && !empty($smtp['password']);

$sent = false;

if ($useSmtp) {
    /* ---- SMTP 送信 (PHPMailer) ---- */
    try {
        $mail = new \PHPMailer\PHPMailer\PHPMailer(true);
        $mail->isSMTP();
        $mail->Host = (string)$smtp['host'];
        $mail->Port = (int)($smtp['port'] ?? 587);
        $mail->SMTPAuth = true;
        $mail->Username = (string)$smtp['username'];
        $mail->Password = (string)$smtp['password'];
        $mail->SMTPAutoTLS = true;
        $mail->Timeout = 15;
        $mail->CharSet = 'UTF-8';
        $mail->Encoding = 'base64';
        $secure = strtolower((string)($smtp['secure'] ?? 'tls'));
        if ($secure === 'ssl') {
            $mail->SMTPSecure = \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS;
        } elseif ($secure === 'tls' || $secure === 'starttls') {
            $mail->SMTPSecure = \PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
        } else {
            $mail->SMTPSecure = '';
        }
        $mail->setFrom($from, $fromName);
        $mail->addReplyTo($email, $name);
        foreach ($toList as $recipient) {
            $recipient = trim((string)$recipient);
            if ($recipient !== '' && filter_var($recipient, FILTER_VALIDATE_EMAIL)) {
                $mail->addAddress($recipient);
            }
        }
        foreach ($ccList as $cc) {
            $cc = trim((string)$cc);
            if ($cc !== '' && filter_var($cc, FILTER_VALIDATE_EMAIL)) {
                $mail->addCC($cc);
            }
        }
        $mail->Subject = $subject;
        $mail->Body = $body;
        $mail->isHTML(false);
        $sent = $mail->send();
    } catch (\Throwable $e) {
        error_log('[intern-entry] SMTP send failed: ' . $e->getMessage());
        $sent = false;
    }
} else {
    /* ---- フォールバック: mb_send_mail ---- */
    $headers = [
        'From: ' . mb_encode_mimeheader($fromName) . ' <' . $from . '>',
        'Reply-To: ' . $email,
        'Content-Type: text/plain; charset=UTF-8',
    ];
    foreach ($ccList as $cc) {
        $cc = trim((string)$cc);
        if ($cc !== '' && filter_var($cc, FILTER_VALIDATE_EMAIL)) {
            $headers[] = 'Cc: ' . $cc;
        }
    }
    $to = implode(', ', array_filter($toList, static fn($r): bool => filter_var(trim((string)$r), FILTER_VALIDATE_EMAIL) !== false));
    if ($to !== '') {
        $sent = function_exists('mb_send_mail')
            ? mb_send_mail($to, $subject, $body, implode("\r\n", $headers))
            : mail($to, $subject, $body, implode("\r\n", $headers));
    }
}

header('Location: ' . ($sent ? 'intern-thanks.html' : 'intern-error.html?form=intern'));
exit;
