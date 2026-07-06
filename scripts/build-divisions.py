#!/usr/bin/env python3
"""採用サイトのディビジョン(部門)ページを生成する。
recruit/division/<slug>.html を出力。共通ヘッダー/フッターを一元管理。
使い方: python3 scripts/build-divisions.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "recruit" / "division"
OUT.mkdir(parents=True, exist_ok=True)

# division: slug, code, name_jp, name_en, hero_img, global(bool), lead, mission[], positions[(title, desc)], interview(url,label) or None
DIVISIONS = [
    {
        "slug": "product",
        "code": "R&D / BUYING",
        "jp": "商品開発・企画部門",
        "en": "PRODUCT DEVELOPMENT",
        "img": "../../assets/img/recruit-division-product-hero.jpg",
        "global": True,
        "lead": "世界から商品を発掘し、日本のヒットを生む。次世代モビリティを、ゼロからつくる。",
        "body": "部品商社の枠を超え「企画から販売まで」を担うカスタムジャパンの心臓部です。世界中からバイク・自転車・自動車の部品や用品、工具、ケミカルを探し出し、商品化・仕入れ・販売までを一気通貫で手がけます。さらに、クルマやバイクの枠を超えた「まだ世の中にないモビリティ」の開発にも挑戦。海外との取引が多く、多国籍のメンバーが活躍している部門です。",
        "mission": [
            ("売れる商品を見抜く", "「お客様がまだ気づいていないニーズ」を形にする発想力。自分が調達した商品が大ヒットしたときの喜びは、この仕事ならではです。"),
            ("世界を相手に交渉する", "海外の現地を訪れ、メーカーや代理店と直接交渉。異文化を楽しみながら、グローバルなビジネスの最前線に立てます。"),
            ("未来の移動を創る", "少子高齢化やライフスタイルの変化で、移動のニーズは多様化。ニッチな課題にこそチャンスがあり、そこへ切り込んでいけるのが強みです。"),
        ],
        "positions": [
            ("次世代モビリティ開発・企画、品質管理", "eXsをはじめ、国内外の動向を読み取りながら次世代モビリティを形にする開発・企画職。"),
            ("海外バイヤー（商品開発・企画、仕入・品質管理）", "世界に眠る“まだ知られていない商品”を発掘し、日本のお客様へ届ける仕事。"),
            ("国内バイヤー（仕入・交渉・管理、販売企画）", "新規仕入先の開拓から販促・ブランディングまで、多くの判断と決断を担うバイヤー業務。"),
        ],
        "interview": ("../index.html#people", "INTERVIEW 04 — 次世代モビリティ / M.K."),
        "interview2": ("../index.html#people", "INTERVIEW 02 — 商品開発・企画 / Y.N."),
    },
    {
        "slug": "global",
        "code": "GLOBAL",
        "jp": "海外事業部",
        "en": "GLOBAL BUSINESS",
        "img": "../../assets/img/recruit-division-global-hero.jpg",
        "global": True,
        "lead": "アジア市場を舞台に、まだ正解のない事業を、自分の手で形にする。",
        "body": "ASEANを中心とした海外市場で新たな事業機会を創出し、グループの成長を推進する部門です。ベトナム・カンボジア・フィリピン・インドネシア、そして中国・台湾を対象に、海外メーカーや代理店、販売店との関係を築きます。代理店営業や販路開拓だけでなく、越境ECやデジタルマーケティングなど新しい販売チャネルの構築にも挑戦。市場調査から商品企画、ブランド展開、販売戦略の立案まで幅広く関わります。",
        "mission": [
            ("正解のない市場で、決める", "自ら考え、行動し、事業を形にするポジション。海外で事業づくりに挑戦したい方に、大きな成長機会があります。"),
            ("チャネルを、新しくつくる", "従来の代理店営業に加え、越境EC・デジタルマーケティングなど、これからの販売チャネルを立ち上げます。"),
            ("社内を横断して動かす", "マーケティング・物流・商品開発の各部門と連携し、海外事業を一気通貫で推進していきます。"),
        ],
        "positions": [
            ("海外事業部（海外営業・事業開発）", "ASEAN・中国・台湾での代理店開拓、越境EC構築、市場調査から販売戦略立案まで。"),
        ],
        "interview": ("../index.html#people", "INTERVIEW 07 — 商品開発・企画 / S.Y."),
        "interview2": None,
    },
    {
        "slug": "marketing",
        "code": "MARKETING",
        "jp": "マーケティング部門",
        "en": "MARKETING",
        "img": "../../assets/img/recruit-division-marketing-hero.jpg",
        "global": False,
        "lead": "13万人の会員と50万SKU。データを起点に、EC事業の成長を牽引する。",
        "body": "BtoB/BtoC向けに自社ECサイトや通販モールの運営、紙カタログやDMを活用したマーケティングを推進しています。基幹システムから取得したデータを活用し、BIツールによるデータ分析基盤を整備。今後はMAツールを使ったシナリオマーケティングを導入し、データを起点とした顧客体験の最適化を目指しています。",
        "mission": [
            ("データで、意思決定する", "勘や経験だけに頼らず、BIツールで可視化したデータをもとに施策を組み立て、成果を検証します。"),
            ("BtoBとBtoC、両方を動かす", "プロショップ向けの卸売とエンドユーザー向けのEC、両方のマーケティングに携われる幅広さがあります。"),
            ("新しい手法を、導入する", "MAツールによるシナリオマーケティングなど、新しい仕組みを自分たちの手で立ち上げるフェーズです。"),
        ],
        "positions": [
            ("BtoB/BtoC マーケティング・プロモーションプランナー", "ECサイト・通販モール・紙カタログ/DMの運営と、データドリブンな施策設計。"),
            ("ECサイトの受発注オペレーター", "注文処理・発送手配・問い合わせ対応に加え、スタッフマネジメントも担う運営職。"),
        ],
        "interview": ("../index.html#people", "INTERVIEW 06 — マーケティングB2C / A.H."),
        "interview2": None,
    },
    {
        "slug": "ict",
        "code": "ENGINEERING",
        "jp": "ICT・エンジニアリング部門",
        "en": "ICT & ENGINEERING",
        "img": "../../assets/img/recruit-division-ict-hero.jpg",
        "global": False,
        "lead": "“最もレガシーな乗り物業界”で、世界一のECサービスをつくる。",
        "body": "バイク業界は“最もレガシーな乗り物業界”とも言われますが、私たちはそこで最先端の開発に挑戦しています。その代表例が、世界最大級のバイク適合データベースを元にした「バイク適合検索」。半世紀以上にわたり積み重ねた部品販売と適合情報をもとに、どのパーツがどのバイクに合うのかを瞬時に検索できる仕組みを実現しました。最先端のヘッドレスECシステムを自社構築し、No.1専門ECサイトへの挑戦を進めています。",
        "mission": [
            ("世界最大級のデータを、動かす", "半世紀分の部品・適合情報という独自資産。これはAI時代に価値が高まる、他社が真似できないデータです。"),
            ("自分たちで、設計する", "ヘッドレスECを内製。「すべての部品と車両をつなぐ世界一のECサービスをつくる」ミッションに挑みます。"),
            ("ICTで、全部門を支える", "業務改善とシステム構築を通じて、社内の生産性を高める縁の下の力持ちの役割も担います。"),
        ],
        "positions": [
            ("フロントエンド・クラウドエンジニア", "世界最大級のバイク適合DBとヘッドレスECを自社開発するエンジニア。"),
            ("社内SE・情報システム管理", "社内システム・ネットワークの構築と改善で、全部門の業務を支える。"),
        ],
        "interview": ("../index.html#people", "INTERVIEW 05 — ICT / T.S."),
        "interview2": None,
    },
    {
        "slug": "scm",
        "code": "LOGISTICS",
        "jp": "SCM・フルフィルメント部門",
        "en": "SCM & FULFILLMENT",
        "img": "../../assets/img/recruit-division-scm-hero.jpg",
        "global": False,
        "lead": "当日出荷を支える、物流の心臓部。現場の声を、仕組みに変える。",
        "body": "国内外の物流拠点と自社システムでサプライチェーン全体をコントロールし、在庫品の当日出荷を実現しています。85万点の商品を、確実に・スムーズにお客様へ届ける——プロの調達を止めないための、事業の根幹を担う部門です。現場で気づいた改善点が、そのまま全社の仕組みになっていくダイナミズムがあります。",
        "mission": [
            ("現場を、仕組みに変える", "日々の気づきや「先読み」が、業務フローやシステムの改善に直結。改善提案が歓迎される文化です。"),
            ("物理世界の強みを、磨く", "AIには代替できない、モノを動かす物流網。50万SKU・当日出荷という競争力の源泉を支えます。"),
            ("チームで、支える", "アルバイトスタッフのマネジメントを含め、組織全体を動かす視点が身につきます。"),
        ],
        "positions": [
            ("物流オペレーター", "ロジスティクスセンターで当日出荷を支える現場職。改善提案が仕組みになります。"),
        ],
        "interview": ("../index.html#people", "INTERVIEW 01 — SCMフルフィルメント / K.I."),
        "interview2": ("../index.html#people", "INTERVIEW 03 — SCMフルフィルメント / N.T."),
    },
    {
        "slug": "corporate",
        "code": "CORPORATE",
        "jp": "コーポレート部門",
        "en": "CORPORATE",
        "img": "../../assets/img/recruit-division-corporate-hero.jpg",
        "global": False,
        "lead": "成長する会社の、土台をつくる。制度づくりから携われるフェーズ。",
        "body": "経理・総務・人事として、会社の成長を足元から支える部門です。創業20年・社員107名、いままさに事業を拡大しているフェーズだからこそ、既存業務を回すだけでなく、制度や仕組みそのものを一緒につくっていく面白さがあります。挑戦を続ける現場を、安心して働ける環境で支える役割です。",
        "mission": [
            ("制度を、つくる", "拡大フェーズの会社で、働きやすい環境づくり(年間休日125日・DX推進など)を自らの手で整えます。"),
            ("全部門と、つながる", "経理・総務・人事は全社の情報が集まる場所。会社全体を俯瞰する視点が養われます。"),
            ("挑戦を、支える", "攻めの事業を、守りの盤石さで支える。安心と挑戦の両立を担う要のポジションです。"),
        ],
        "positions": [
            ("経理・総務・人事", "会社の成長を支えるコーポレート業務。制度づくりから携われます。"),
        ],
        "interview": None,
        "interview2": None,
    },
]

NAV = [("../index.html", "RECRUIT TOP"), ("../index.html#jobs", "JOBS"),
       ("../index.html#people", "PEOPLE"), ("../index.html#benefits", "BENEFITS")]


def page(d, others):
    nav = "\n".join(f'    <a href="{h}">{t}</a>' for h, t in NAV)
    tag = '<span class="dv-tag dv-tag--global">GLOBAL — 海外との取引が多い部門</span>' if d["global"] else ""
    mission = "\n".join(
        f'      <div class="dv-mission reveal"><h3>{m[0]}</h3><p>{m[1]}</p></div>' for m in d["mission"]
    )
    positions = "\n".join(
        f'      <div class="dv-pos reveal"><h3>{p[0]}</h3><p>{p[1]}</p></div>' for p in d["positions"]
    )
    ivs = [x for x in [d.get("interview"), d.get("interview2")] if x]
    iv_html = ""
    if ivs:
        cards = "\n".join(
            f'      <a class="dv-iv reveal" href="../index.html#people"><span>▶ 社員インタビュー</span>{lb}</a>'
            for u, lb in ivs
        )
        iv_html = f'''
<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">VOICE</p>
    <h2 class="sec-title sec-title--sm reveal">この部門で働くひと</h2>
    <div class="dv-iv-list">
{cards}
    </div>
  </div>
</section>'''
    # other divisions nav
    other_links = "\n".join(
        f'      <a class="dv-other reveal" href="{o["slug"]}.html"><b>{o["en"]}</b><span>{o["jp"]}</span></a>'
        for o in others
    )
    gtag_note = ""
    if d["global"]:
        gtag_note = '<p class="reveal" style="margin-top:22px;font-size:12.5px"><a href="../global.html" style="color:var(--c-blue);text-decoration:underline">海外出身の方へ — この部門で活躍できます（応募には日本語能力試験N1が必要です）</a></p>'
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['jp']} | 採用情報 株式会社カスタムジャパン</title>
<meta name="description" content="カスタムジャパン {d['jp']}の仕事紹介。{d['lead']}">
<link rel="icon" href="../../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/style.css">
<style>
.dv-hero{{position:relative;min-height:64svh;display:flex;align-items:flex-end;overflow:hidden;background:var(--c-dark);color:#fff}}
.dv-hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.42}}
.dv-hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(8,10,14,.9) 0%,rgba(8,10,14,.25) 65%)}}
.dv-hero__inner{{position:relative;z-index:2;padding:20vh 6vw 8vh;width:100%}}
.dv-hero__code{{font-family:var(--font-en);font-weight:800;font-size:12px;letter-spacing:.34em;color:#ff6b6a;margin-bottom:16px}}
.dv-hero__title{{font-size:clamp(28px,4.6vw,52px);font-weight:900;letter-spacing:.04em;line-height:1.4}}
.dv-hero__en{{font-family:var(--font-en);font-weight:600;font-size:12px;letter-spacing:.2em;color:rgba(255,255,255,.6);margin-top:12px}}
.dv-tag{{display:inline-block;margin-top:20px;font-size:11.5px;font-weight:700;border-radius:100px;padding:6px 16px}}
.dv-tag--global{{background:var(--c-red);color:#fff}}
.dv-lead{{font-size:clamp(19px,2.4vw,30px);font-weight:900;line-height:1.8;letter-spacing:.04em;max-width:900px;margin-bottom:32px}}
.dv-body{{max-width:820px;font-size:13.5px;color:#3c4149;line-height:2.2}}
.dv-missions{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
@media(max-width:768px){{.dv-missions{{grid-template-columns:1fr}}}}
.dv-mission{{border:1px solid var(--c-line);border-radius:16px;padding:30px 28px;background:var(--c-white)}}
.dv-mission h3{{font-size:16px;font-weight:900;margin-bottom:10px;line-height:1.6}}
.dv-mission p{{font-size:12.5px;color:#3c4149;line-height:2}}
.dv-positions{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;max-width:1000px}}
@media(max-width:768px){{.dv-positions{{grid-template-columns:1fr}}}}
.dv-pos{{border:1px solid var(--c-line);border-left:3px solid var(--c-blue);border-radius:12px;padding:24px 26px;background:var(--c-white)}}
.dv-pos h3{{font-size:14.5px;font-weight:700;margin-bottom:8px;line-height:1.7}}
.dv-pos p{{font-size:12px;color:#3c4149;line-height:1.9}}
.dv-iv-list{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;max-width:1000px}}
@media(max-width:768px){{.dv-iv-list{{grid-template-columns:1fr}}}}
.dv-iv{{display:flex;flex-direction:column;gap:8px;border:1px solid var(--c-line);border-radius:14px;padding:26px 28px;background:var(--c-white);font-size:13.5px;font-weight:700;line-height:1.7;transition:transform .35s var(--ease),box-shadow .35s}}
.dv-iv:hover{{transform:translateY(-3px);box-shadow:0 14px 32px rgba(13,15,18,.09)}}
.dv-iv span{{font-family:var(--font-en);font-size:10.5px;font-weight:800;letter-spacing:.18em;color:var(--c-red)}}
.dv-others{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
@media(max-width:768px){{.dv-others{{grid-template-columns:1fr}}}}
.dv-other{{border:1px solid var(--c-line);border-radius:12px;padding:20px 22px;background:var(--c-white);transition:border-color .3s,transform .3s}}
.dv-other:hover{{border-color:var(--c-blue);transform:translateY(-2px)}}
.dv-other b{{font-family:var(--font-en);font-weight:800;font-size:12px;letter-spacing:.14em;color:var(--c-blue);display:block;margin-bottom:4px}}
.dv-other span{{font-size:12px;color:#3c4149}}
</style>
</head>
<body>

<header class="header header--solid" id="header">
  <a href="../../index.html" class="header__logo">
    <img src="../../assets/logo/cj-logo-white-text.svg" alt="" class="header__logo-white" aria-hidden="true">
    <img src="../../assets/logo/cj-logo-black-text.svg" alt="株式会社カスタムジャパン" class="header__logo-color">
  </a>
  <nav class="header__nav">
{nav}
    <a href="../en/division/{d['slug']}.html" class="header__lang">EN</a>
    <a href="../index.html#entry" class="header__recruit">
      <span class="header__recruit-en">ENTRY</span>
      <span class="header__recruit-jp">応募する</span>
    </a>
  </nav>
  <button class="header__menu-btn" id="menuBtn" aria-controls="mobileMenu" aria-expanded="false" aria-label="メニュー"><span></span><span></span></button>
</header>

<div class="mobile-menu" id="mobileMenu">
  <nav>
{nav}
    <a href="../en/division/{d['slug']}.html">EN — English</a>
    <a href="../index.html#entry" class="mobile-menu__recruit">ENTRY — 応募する</a>
  </nav>
</div>

<button class="mascot-top" id="mascotTop" aria-label="ページの先頭へ戻る">
  <img src="../../assets/logo/cj-mascot.svg" alt="">
  <span>TOP</span>
</button>

<main>

<section class="dv-hero">
  <img src="{d['img']}" alt="">
  <div class="dv-hero__inner">
    <p class="dv-hero__code">{d['code']}</p>
    <h1 class="dv-hero__title">{d['jp']}</h1>
    <p class="dv-hero__en">{d['en']}</p>
    {tag}
  </div>
</section>
<div class="crumb"><a href="../../index.html">企業サイト</a><span>/</span><a href="../index.html">採用情報</a><span>/</span>{d['jp']}</div>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OVERVIEW</p>
    <p class="dv-lead reveal">{d['lead']}</p>
    <p class="dv-body reveal">{d['body']}</p>
    {gtag_note}
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">WHAT MAKES IT EXCITING</p>
    <h2 class="sec-title sec-title--sm reveal">この部門の、面白さ</h2>
    <div class="dv-missions">
{mission}
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">POSITIONS</p>
    <h2 class="sec-title sec-title--sm reveal">募集ポジション</h2>
    <div class="dv-positions">
{positions}
    </div>
    <p class="reveal" style="margin-top:36px"><a href="../index.html#entry" class="btn-solid">この部門に応募する</a></p>
  </div>
</section>
{iv_html}

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OTHER DIVISIONS</p>
    <h2 class="sec-title sec-title--sm reveal">ほかの部門を見る</h2>
    <div class="dv-others">
{other_links}
    </div>
  </div>
</section>

<footer class="footer">
  <div class="inner">
    <div class="footer__top">
      <div class="footer__company">
        <img src="../../assets/logo/cj-logo-white-text.svg" alt="CUSTOM JAPAN" class="footer__logo">
        <p class="footer__address">株式会社カスタムジャパン<br>〒542-0073 大阪市中央区日本橋2-9-16 日本橋センタービル6F<br>採用窓口 recruit@customjapan.jp</p>
      </div>
      <nav class="footer__nav">
        <a href="../index.html">RECRUIT TOP</a>
        <a href="../index.html#jobs">JOBS</a>
        <a href="../index.html#people">PEOPLE</a>
        <a href="../global.html">GLOBAL</a>
        <a href="../../index.html">企業サイト</a>
      </nav>
      <div class="footer__contact">
        <p>ご応募はこちら</p>
        <a href="../index.html#entry" class="btn-line btn-line--light">エントリー</a>
      </div>
    </div>
    <p class="footer__copy">&copy; Custom Japan Co., Ltd. All Rights Reserved.</p>
  </div>
</footer>

</main>

<script src="../../js/vendor/gsap.min.js"></script>
<script src="../../js/vendor/ScrollTrigger.min.js"></script>
<script src="../../js/vendor/lenis.min.js"></script>
<script src="../../js/main.js"></script>
</body>
</html>
"""


for d in DIVISIONS:
    others = [o for o in DIVISIONS if o["slug"] != d["slug"]]
    (OUT / f"{d['slug']}.html").write_text(page(d, others), encoding="utf-8")
    print("wrote", OUT / f"{d['slug']}.html")
