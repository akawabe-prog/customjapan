<?php
declare(strict_types=1);

/**
 * 長期インターン カジュアル面談 受信ハンドラ（最小項目版）
 * 大学・学部・名前 + 連絡用メール。intern-entry.php と同じ送信方式。
 */

header('X-Frame-Options: SAMEORIGIN');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');

if (($_SERVER['REQUEST_METHOD'] ?? 'GET') !== 'POST') {
    header('Location: casual.html');
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
            return true;
        }
        $host = strtolower((string)parse_url($url, PHP_URL_HOST));
        return $host !== '' && in_array($host, $allowedHosts, true);
    };
    return $check(trim((string)($_SERVER['HTTP_ORIGIN'] ?? '')))
        && $check(trim((string)($_SERVER['HTTP_REFERER'] ?? '')));
}

/* ---- 入力取得 ---- */
$name    = posted('name');
$grade   = posted('grade');
$school  = posted('school');
$faculty = posted('faculty');
$email   = posted('email');
$privacy = posted('privacy');

/* ---- スパム対策 ---- */
$honeypot      = posted('company_hp');
$jsEnabled     = posted('js_enabled');
$csrfToken     = posted('csrf_token');
$formStartedAt = (int)posted('form_started_at');

/* ---- バリデーション ---- */
$errors = [];
$now = time();

if ($name === '' || mb_strlen($name) > 80 || preg_match('/[\r\n]/', $name)) {
    $errors[] = 'name';
}
if ($grade === '' || mb_strlen($grade) > 40) {
    $errors[] = 'grade';
}
if ($school === '' || mb_strlen($school) > 120 || preg_match('/[\r\n]/', $school)) {
    $errors[] = 'school';
}
// 高卒・その他は学部/学科が無いため任意
$facultyOptional = in_array($grade, ['高卒', 'その他'], true);
if (mb_strlen($faculty) > 120 || preg_match('/[\r\n]/', $faculty)) {
    $errors[] = 'faculty';
} elseif (!$facultyOptional && $faculty === '') {
    $errors[] = 'faculty';
}
if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || mb_strlen($email) > 255 || preg_match('/[\r\n]/', $email)) {
    $errors[] = 'email';
}
if ($privacy !== '1') {
    $errors[] = 'privacy';
}

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
if ($formStartedAt <= 0 || ($now - $formStartedAt) < 1 || ($now - $formStartedAt) > 7200) {
    $errors[] = 'time';
}

if (!empty($errors)) {
    header('Location: intern-error.html?type=casual');
    exit;
}

/* ---- メール本文 ---- */
$ip = (string)($_SERVER['REMOTE_ADDR'] ?? 'unknown');
$ua = substr((string)($_SERVER['HTTP_USER_AGENT'] ?? ''), 0, 180);

$subject = '【カスタムジャパン】長期インターン カジュアル面談 希望';
$body = implode("\n", [
    '長期インターンのカジュアル面談 申し込みがありました。',
    '',
    'お名前: ' . $name,
    '現在の区分・学年: ' . $grade,
    '大学・学校名: ' . $school,
    '学部・学科: ' . ($faculty !== '' ? $faculty : '(該当なし)'),
    'メールアドレス: ' . $email,
    '',
    '---',
    '送信元IP: ' . $ip,
    'UA: ' . $ua,
    'Referer: ' . (string)($_SERVER['HTTP_REFERER'] ?? '-'),
]);

/* ---- 設定ロード (intern-entry と共通の設定ファイルを流用) ---- */
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
        error_log('[casual-entry] SMTP send failed: ' . $e->getMessage());
        $sent = false;
    }
} else {
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

header('Location: ' . ($sent ? 'intern-thanks.html?type=casual' : 'intern-error.html?type=casual'));
exit;
