#!/usr/bin/env python3
"""SMART RIDE DASHBOARD (SRD 5) — 独立ブランドサイトを生成する。
コーポレート下層ではなく、単独ブランドサイトのデザイン(専用ヘッダー/フッター・ダーク基調)。
出力: smart/index.html(ブランドLP) + smart/{slug}.html(4商品)
データ: data/smart-specs.json / 看板画像: assets/img/smart/{id}/main.jpg
CSS: css/style.css(トークン/reveal/フォント) + css/smart.css(ブランド専用)
使い方: python3 scripts/build-smart.py
"""
import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "smart"
OUT.mkdir(exist_ok=True)
DATA = json.loads((ROOT / "data" / "smart-specs.json").read_text(encoding="utf-8"))
BASE = "https://customjapan.jp"
SERIES = DATA["series"]
MODELS = DATA["models"]
BUY = "https://www.customjapan.net/item/{id}"
SHOP = "https://www.customjapan.net/search?q=SRD5"
IMG = "../assets/img/smart/{id}/main.jpg"

def esc(s): return html.escape(str(s))
def yen(n): return f"¥{n:,}"
def by_slug(s): return next(m for m in MODELS if m["slug"] == s)

HEADER = """
<header class="srd-header" id="srdHeader">
  <a class="srd-header__brand" href="index.html">SRD<b>5</b><span>SMART RIDE DASHBOARD</span></a>
  <nav class="srd-header__nav" id="srdNav">
    <a href="index.html#lineup">LINEUP</a>
    <a href="index.html#compare">比較</a>
    <a href="index.html#story">特長</a>
    <a href="{shop}" target="_blank" rel="noopener" class="srd-buy">購入</a>
  </nav>
  <span class="srd-header__cj">by <a href="../index.html">Custom Japan</a></span>
  <button class="srd-header__menu" id="srdMenu" aria-label="メニュー"><span></span><span></span><span></span></button>
</header>""".replace("{shop}", SHOP)

def footer():
    models = "\n".join(f'        <a href="{m["slug"]}.html">{esc(m["name"])}</a>' for m in MODELS)
    return f"""
<footer class="srd-footer">
  <div class="srd-footer__top">
    <div class="srd-footer__brand">
      <b>SRD<span>5</span></b>
      <p>スマートライドダッシュボード SRD 5 シリーズ。CarPlay・Android Auto を軸に、ライドの体験をひとつに束ねるオールインワン・ダッシュボード。株式会社カスタムジャパンが自社開発しています。</p>
    </div>
    <div class="srd-footer__cols">
      <div class="srd-footer__col">
        <h4>LINEUP</h4>
{models}
      </div>
      <div class="srd-footer__col">
        <h4>SHOP</h4>
        <a href="{SHOP}" target="_blank" rel="noopener">公式通販で購入</a>
        <a href="index.html#compare">スペック比較</a>
      </div>
      <div class="srd-footer__col">
        <h4>CUSTOM JAPAN</h4>
        <a href="../index.html">企業サイト</a>
        <a href="../brands.html">ブランド一覧</a>
        <a href="../contact.html">お問い合わせ</a>
      </div>
    </div>
  </div>
  <div class="srd-footer__bottom">
    <span>&copy; Custom Japan Co., Ltd. All Rights Reserved.</span>
    <span>SMART RIDE DASHBOARD is a product brand of <a href="../index.html">Custom Japan</a>.</span>
  </div>
</footer>"""

SCRIPTS = """
<script src="../js/vendor/gsap.min.js"></script>
<script src="../js/vendor/ScrollTrigger.min.js"></script>
<script src="../js/vendor/lenis.min.js"></script>
<script src="../js/main.js"></script>
<script>
(function(){
  var h=document.getElementById('srdHeader'),b=document.getElementById('srdMenu'),n=document.getElementById('srdNav');
  if(h){addEventListener('scroll',function(){h.classList.toggle('is-scrolled',window.scrollY>40);},{passive:true});}
  if(b&&n){b.addEventListener('click',function(){n.classList.toggle('is-open');});
    n.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){n.classList.remove('is-open');});});}
})();
</script>
</body>
</html>"""

def head(title, desc, canon, og_img):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="icon" href="../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<link rel="stylesheet" href="../css/smart.css">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="SMART RIDE DASHBOARD | Custom Japan">
<meta property="og:locale" content="ja_JP">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:image" content="{og_img}">
</head>
<body>
<main class="srd-site">"""

# spec keys (first model order) + cell renderer
SPEC_KEYS = list(MODELS[0]["specs"].keys())
def cell(v):
    if v.startswith("×"): return '<span class="no">—</span>'
    if v.startswith("◎"): return f'<span class="yes">{esc(v)}</span>'
    return esc(v)

# ============ BRAND LP ============
def build_lp():
    pro, std, slim = by_slug("srd5-pro"), by_slug("srd5"), by_slug("srd5-slim")
    # feature showcase blocks (reuse product renders)
    features = [
        ("01", std, "すべてを、ひとつに。", "CarPlay・Android Auto のワイヤレス連携、前後フルHDドライブレコーダー、タイヤ空気圧モニタリング、GPS。ツーリングに必要な機能を1台のダッシュボードへ統合しました。スマホを取り出さずに、ナビも音楽も通話も、大画面で。"),
        ("02", pro, "過酷でも、止まらない。", "最上位 Pro は 1000nit の高輝度 IPS で直射日光下でも視認性抜群。IP67 防水防塵・航空グレードアルミ筐体・信越シリコーン採用で、雨の日も真夏も本領を発揮します。国内電波法「技適」取得済み。"),
        ("03", slim, "選べる、4モデル。", "全部入りの Pro / 標準、スマホ連携に絞った Basic、薄型の Slim。使い方と予算に合わせて選べる4モデルを、すべて5インチ IPS・当日出荷でご用意しています。"),
    ]
    feat_html = ""
    for i, (num, m, h3, p) in enumerate(features):
        rev = " srd-feature--rev" if i % 2 else ""
        feat_html += f"""
<div class="srd-feature{rev}">
  <div class="srd-feature__media is-contain reveal"><img src="{IMG.format(id=m['id'])}" alt="{esc(m['name'])}" loading="lazy"></div>
  <div class="reveal">
    <p class="srd-feature__num">FEATURE {num}</p>
    <h3>{esc(h3)}</h3>
    <p>{esc(p)}</p>
  </div>
</div>"""

    lineup = "\n".join(f"""      <article class="srd-card reveal">
        <div class="srd-card__img"><img src="{IMG.format(id=m['id'])}" alt="{esc(m['name'])}" loading="lazy"></div>
        <div class="srd-card__body">
          <p class="srd-card__tier">{esc(m['tier'])}</p>
          <h3 class="srd-card__name">{esc(m['name'])}</h3>
          <p class="srd-card__catch">{esc(m['catch'])}</p>
          <p class="srd-card__price">{yen(m['price'])}<small>税込</small></p>
          <a href="{m['slug']}.html" class="srd-card__btn">詳しく見る</a>
        </div>
      </article>""" for m in MODELS)

    thead = "<th></th>" + "".join(f'<th><small>{esc(m["tier"])}</small><a href="{m["slug"]}.html">{esc(m["name"])}</a></th>' for m in MODELS)
    price_row = "<th>価格（税込）</th>" + "".join(f'<td>{yen(m["price"])}</td>' for m in MODELS)
    body_rows = ""
    for k in SPEC_KEYS:
        body_rows += "<tr><th>" + esc(k) + "</th>" + "".join(f'<td>{cell(m["specs"].get(k,"—"))}</td>' for m in MODELS) + "</tr>\n          "

    title = "SMART RIDE DASHBOARD SRD 5 | バイク用スマートモニター"
    desc = SERIES["lead"][:110]
    body = f"""
<section class="srd-hero">
  <video class="srd-hero__video" src="../assets/video/smart-srd.mp4" poster="{IMG.format(id=pro['id'])}" autoplay muted loop playsinline preload="auto"></video>
  <div class="srd-hero__inner">
    <p class="srd-hero__label">SMART RIDE DASHBOARD</p>
    <h1 class="srd-hero__title">{esc(SERIES['catch'])}</h1>
    <p class="srd-hero__lead">{esc(SERIES['lead'])}</p>
    <div class="srd-hero__cta">
      <a href="#lineup" class="srd-btn srd-btn--fill">ラインナップを見る</a>
      <a href="{SHOP}" target="_blank" rel="noopener" class="srd-btn srd-btn--ghost">公式通販で見る</a>
    </div>
  </div>
  <span class="srd-scroll">SCROLL</span>
</section>

<section class="srd-sec srd-statement" id="story">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal" style="text-align:center">THE CONCEPT</p>
    <p class="srd-big reveal">スマホは、ポケットへ。<br><em>ライドに必要なすべて</em>を、<br>ハンドルの上に。</p>
  </div>
</section>
{feat_html}

<section class="srd-sec" id="lineup">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal">LINEUP</p>
    <h2 class="srd-h2 reveal">用途と予算で選ぶ、4モデル。</h2>
    <p class="srd-lead reveal">すべて5インチ IPS・国内技適取得・当日出荷。あなたのバイクライフに合う一台を。</p>
    <div class="srd-lineup">
{lineup}
    </div>
  </div>
</section>

<section class="srd-sec" id="compare" style="background:#0e1116">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal">COMPARE</p>
    <h2 class="srd-h2 reveal">スペック比較</h2>
    <div class="srd-compare reveal">
      <table>
        <thead><tr>{thead}</tr></thead>
        <tbody>
          <tr class="price-row">{price_row}</tr>
          {body_rows}</tbody>
      </table>
    </div>
    <p class="srd-note">※ 価格・仕様は公式通販サイト掲載時点の情報です。最新情報は各商品ページをご確認ください。</p>
  </div>
</section>

<section class="srd-sec srd-buyband">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal" style="text-align:center">WHERE TO BUY</p>
    <h2 class="srd-h2 reveal">ご購入はこちら</h2>
    <p class="srd-lead reveal" style="margin-left:auto;margin-right:auto;text-align:center">カスタムジャパン公式通販サイトからご購入いただけます。在庫品は16時までのご注文で当日出荷。</p>
    <div class="reveal" style="margin-top:32px;display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a href="{SHOP}" target="_blank" rel="noopener" class="srd-btn srd-btn--fill">SRD 5 シリーズを見る</a>
    </div>
  </div>
</section>
"""
    doc = head(title, desc, f"{BASE}/smart/", f"{BASE}/{IMG.format(id=pro['id'])[3:]}") + HEADER + body + footer() + SCRIPTS
    (OUT / "index.html").write_text(doc, encoding="utf-8")
    print("wrote", OUT / "index.html")

# ============ PRODUCT PAGE ============
def build_product(m):
    others = [x for x in MODELS if x["slug"] != m["slug"]]
    hl = "\n".join(f"""      <div class="srd-hl__item reveal"><h3>{esc(t)}</h3><p>{esc(d)}</p></div>""" for t, d in m["highlights"])
    spec_rows = "\n".join(f"        <tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in m["specs"].items())
    others_html = "\n".join(f"""      <a class="srd-other reveal" href="{o['slug']}.html"><img src="{IMG.format(id=o['id'])}" alt=""><span><b>{esc(o['name'])}</b><br><span>{esc(o['tierJp'])} / {yen(o['price'])}</span></span></a>""" for o in others)
    title = f"{m['name']} | SMART RIDE DASHBOARD SRD 5"
    desc = m["catch"]
    body = f"""
<section class="srd-phero">
  <div class="srd-phero__grid">
    <div class="srd-phero__img reveal"><img src="{IMG.format(id=m['id'])}" alt="{esc(m['name'])}"></div>
    <div>
      <p class="srd-phero__tier reveal">SMART RIDE DASHBOARD ・ {esc(m['tier'])}</p>
      <h1 class="srd-phero__name reveal">{esc(m['name'])}</h1>
      <p class="srd-phero__catch reveal">{esc(m['catch'])}</p>
      <p class="srd-phero__price reveal">{yen(m['price'])}<small>税込</small></p>
      <div class="srd-phero__cta reveal">
        <a href="{BUY.format(id=m['id'])}" target="_blank" rel="noopener" class="srd-btn srd-btn--fill">公式通販で購入</a>
        <a href="index.html" class="srd-btn srd-btn--ghost">シリーズ一覧</a>
      </div>
    </div>
  </div>
</section>

<section class="srd-sec srd-statement srd-sec--tight">
  <div class="srd-inner">
    <p class="srd-big reveal" style="font-size:clamp(20px,3vw,34px)">{esc(m['tagline'])}</p>
  </div>
</section>

<section class="srd-sec" style="background:#0e1116">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal">FEATURES</p>
    <h2 class="srd-h2 reveal">おもな特長</h2>
    <div class="srd-hl">
{hl}
    </div>
  </div>
</section>

<section class="srd-sec">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal">SPECIFICATIONS</p>
    <h2 class="srd-h2 reveal">製品仕様</h2>
    <div class="srd-spec reveal">
      <table>
{spec_rows}
      </table>
    </div>
    <div class="reveal" style="margin-top:34px;display:flex;gap:14px;flex-wrap:wrap">
      <a href="{BUY.format(id=m['id'])}" target="_blank" rel="noopener" class="srd-btn srd-btn--fill">公式通販で購入（{yen(m['price'])}）</a>
      <a href="index.html#compare" class="srd-btn srd-btn--ghost">他モデルと比較</a>
    </div>
  </div>
</section>

<section class="srd-sec" style="background:#0e1116">
  <div class="srd-inner">
    <p class="srd-eyebrow reveal">OTHER MODELS</p>
    <h2 class="srd-h2 reveal">ほかのモデル</h2>
    <div class="srd-others">
{others_html}
    </div>
  </div>
</section>
"""
    doc = head(title, desc, f"{BASE}/smart/{m['slug']}.html", f"{BASE}/{IMG.format(id=m['id'])[3:]}") + HEADER + body + footer() + SCRIPTS
    (OUT / f"{m['slug']}.html").write_text(doc, encoding="utf-8")
    print("wrote", OUT / f"{m['slug']}.html")

build_lp()
for m in MODELS:
    build_product(m)
print("--- done ---")
