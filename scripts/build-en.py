#!/usr/bin/env python3
"""英語版ページ(en/*.html)を生成する。

日本語ページと同じデザイン/クラスを使い、コンテンツのみ英語化。
共通のヘッダー・フッターはこのスクリプトで一元管理する。
使い方: python3 scripts/build-en.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "en"
OUT.mkdir(exist_ok=True)

NAV_ITEMS = [
    ("about.html", "ABOUT"),
    ("business.html", "BUSINESS"),
    ("brands.html", "BRANDS"),
    ("events.html", "EVENTS"),
    ("news.html", "NEWS"),
    ("contact.html", "CONTACT"),
]


def chrome(page, title, desc, body, header_solid=True, with_loader=False):
    nav = "\n".join(f'    <a href="{h}">{t}</a>' for h, t in NAV_ITEMS)
    mnav = "\n".join(f'    <a href="{h}">{t}</a>' for h, t in NAV_ITEMS)
    solid = " header--solid" if header_solid else ""
    loader = (
        '\n<div class="loader" id="loader">\n'
        '  <img src="../assets/logo/cj-logo-h.svg" alt="CUSTOM JAPAN" class="loader__logo">\n'
        '  <div class="loader__bar"><span></span></div>\n'
        "</div>\n"
        if with_loader
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/style.css">
<link rel="alternate" hreflang="ja" href="https://customjapan.jp/{page}">
<link rel="alternate" hreflang="en" href="https://customjapan.jp/en/{page}">
<link rel="alternate" hreflang="x-default" href="https://customjapan.jp/{page}">
</head>
<body>
{loader}
<header class="header{solid}" id="header">
  <a href="index.html" class="header__logo">
    <img src="../assets/logo/cj-logo-white-text.svg" alt="" class="header__logo-white" aria-hidden="true">
    <img src="../assets/logo/cj-logo-black-text.svg" alt="Custom Japan Co., Ltd." class="header__logo-color">
  </a>
  <nav class="header__nav">
{nav}
    <a href="../{page}" class="header__lang">日本語</a>
    <a href="../recruit/index.html" class="header__recruit">
      <span class="header__recruit-en">RECRUIT</span>
      <span class="header__recruit-jp">JP ONLY</span>
    </a>
  </nav>
  <button class="header__menu-btn" id="menuBtn" aria-controls="mobileMenu" aria-expanded="false" aria-label="Menu"><span></span><span></span></button>
</header>

<div class="mobile-menu" id="mobileMenu">
  <nav>
{mnav}
    <a href="../{page}">日本語</a>
    <a href="../recruit/index.html" class="mobile-menu__recruit">RECRUIT (JP)</a>
  </nav>
</div>

<button class="mascot-top" id="mascotTop" aria-label="Back to top">
  <img src="../assets/logo/cj-mascot.svg" alt="">
  <span>TOP</span>
</button>

<main>
{body}

<footer class="footer" id="contact">
  <div class="inner">
    <div class="footer__top">
      <div class="footer__company">
        <img src="../assets/logo/cj-logo-white-text.svg" alt="CUSTOM JAPAN" class="footer__logo">
        <p class="footer__address">Custom Japan Co., Ltd.<br>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>Founded August 9, 2005</p>
      </div>
      <nav class="footer__nav">
{nav}
      </nav>
      <div class="footer__contact">
        <p>Business &amp; general inquiries</p>
        <a href="contact.html" class="btn-line btn-line--light">Contact us</a>
      </div>
    </div>
    <p class="footer__copy">&copy; Custom Japan Co., Ltd. All Rights Reserved.</p>
  </div>
</footer>

</main>

<script src="../js/vendor/gsap.min.js"></script>
<script src="../js/vendor/ScrollTrigger.min.js"></script>
<script src="../js/vendor/lenis.min.js"></script>
<script src="../js/main.js"></script>
</body>
</html>
"""


def page_hero(label, title, jp, crumb):
    return f"""
<section class="page-hero">
  <div class="inner">
    <p class="page-hero__label">{label}</p>
    <h1 class="page-hero__title">{title}</h1>
    <p class="page-hero__jp">{jp}</p>
  </div>
</section>
<div class="crumb"><a href="index.html">TOP</a><span>/</span>{crumb}</div>"""


# ---------------------------------------------------------------- index
INDEX_BODY = """
<section class="hero">
  <div class="hero__bg">
    <video class="hero__video" src="../assets/video/hero.mp4" poster="../assets/img/hero-rider.jpg" autoplay muted loop playsinline></video>
    <div class="hero__overlay"></div>
  </div>
  <div class="hero__content">
    <p class="hero__eyebrow"><span>MOBILITY AFTERMARKET PLATFORM COMPANY</span></p>
    <h1 class="hero__title">
      <span class="hero__line"><span>Ride together,</span></span>
      <span class="hero__line"><span>move forward.</span></span>
    </h1>
    <p class="hero__sub">#ノル人をツクる — from Osaka, Japan</p>
    <p class="hero__desc">We are the B2B distribution platform company supporting <br class="pc">motorcycle, bicycle and automotive professionals across Japan.</p>
  </div>
  <div class="hero__scroll"><span class="hero__scroll-line"></span>SCROLL</div>
</section>

<section class="statement" id="about">
  <div class="inner">
    <p class="sec-label reveal">OUR MISSION</p>
    <h2 class="statement__title">
      <span class="st-line">Riding with 90,000</span>
      <span class="st-line">professionals,</span>
      <span class="st-line">all over Japan.</span>
    </h2>
    <div class="statement__body reveal">
      <p>Our story began in 1954 as a small parts shop in Tsuruhashi, Osaka. Custom Japan carries over 70 years of distribution know-how, operating a B2B platform that delivers parts, accessories and tools for motorcycles, bicycles and automobiles to professional shops nationwide.</p>
      <p>Today we are evolving from a company that delivers products into one that creates them — from next-generation mobility to the distribution of world-leading brands.</p>
    </div>
    <p style="margin-top:48px"><a href="about.html" class="btn-line reveal">More about us</a></p>
  </div>
</section>

<section class="numbers">
  <div class="inner">
    <p class="sec-label reveal">CUSTOM JAPAN IN NUMBERS</p>
    <div class="numbers__grid">
      <div class="num-card reveal">
        <div class="num-card__value"><span class="count" data-count="90000">0</span></div>
        <div class="num-card__label">Registered pro shops</div>
        <div class="num-card__note">Motorcycle, bicycle &amp; car dealers nationwide</div>
      </div>
      <div class="num-card reveal">
        <div class="num-card__value"><span class="count" data-count="500000">0</span><small>+</small></div>
        <div class="num-card__label">SKUs</div>
        <div class="num-card__note">One of the industry's largest databases</div>
      </div>
      <div class="num-card reveal">
        <div class="num-card__value"><span class="count" data-count="90">0</span><small>%</small></div>
        <div class="num-card__label">Usage share of JP bike dealers</div>
        <div class="num-card__note">The standard infrastructure for pros</div>
      </div>
      <div class="num-card reveal">
        <div class="num-card__value"><span class="count" data-count="70">0</span><small>yrs+</small></div>
        <div class="num-card__label">Distribution roots</div>
        <div class="num-card__note">Since Tsuruhashi Buhin, founded 1954</div>
      </div>
    </div>
  </div>
</section>

<section class="business" id="business">
  <div class="inner">
    <p class="sec-label reveal">BUSINESS</p>
    <h2 class="sec-title reveal">Every part a pro needs,<br>on a single platform.</h2>
    <p class="sec-lead reveal">Between global manufacturers and 90,000 professional shops across Japan, Custom Japan handles inventory, logistics and data end to end — with 500,000+ SKUs and same-day shipping for orders placed by 4 p.m.</p>
    <div class="business__flow reveal">
      <div class="flow-node"><em>Global makers<br>&amp; brands</em></div>
      <div class="flow-arrow"></div>
      <div class="flow-node flow-node--center"><strong>CUSTOM JAPAN</strong><em>Inventory / Logistics / Data / R&amp;D</em></div>
      <div class="flow-arrow"></div>
      <div class="flow-node"><em>90,000 pro shops<br>across Japan</em></div>
    </div>
    <p><a href="business.html" class="btn-line reveal">Our business</a></p>
  </div>
  <div class="business__marquee" aria-hidden="true">
    <div class="marquee-track">
      <img src="../assets/img/slide-engine.jpg" alt=""><img src="../assets/img/slide-car.jpg" alt=""><img src="../assets/img/slide-timsun2.jpg" alt=""><img src="../assets/img/slide-shad2.jpg" alt=""><img src="../assets/img/slide_exs_street.webp" alt=""><img src="../assets/img/topslide_campany.jpg" alt="">
      <img src="../assets/img/slide-engine.jpg" alt=""><img src="../assets/img/slide-car.jpg" alt=""><img src="../assets/img/slide-timsun2.jpg" alt=""><img src="../assets/img/slide-shad2.jpg" alt=""><img src="../assets/img/slide_exs_street.webp" alt=""><img src="../assets/img/topslide_campany.jpg" alt="">
    </div>
  </div>
</section>

<section class="strengths-sec" id="strengths">
  <div class="inner">
    <p class="sec-label reveal">OUR STRENGTHS</p>
    <h2 class="sec-title sec-title--sm reveal">Five reasons professionals choose Custom Japan</h2>
    <p class="sec-lead reveal">We back up "find it, choose it, deliver it" with systems. A catalog, Japan's first exact-match parts search, human support, thorough quality control and same-day logistics — five strengths refined over 70 years keep the professional field running.</p>
    <div class="str-slider reveal">
    <div class="str-cards" id="strengthsScroller">
      <article class="str-card reveal">
        <div class="str-card__img"><span class="str-card__num">01</span><img src="../assets/img/recruit-work-catalog.jpg" alt="Staff reviewing the wholesale catalog" loading="lazy"></div>
        <div class="str-card__body">
          <h3>Industry-leading wholesale catalog —<br>print &amp; members-only web</h3>
          <p>A print catalog covering the essential parts for commuting, school and business vehicles, paired with a closed, members-only web catalog that keeps prices off public search engines. Filtering and product-comparison tools, refined daily as our range grows, guide you to the right part fast — across 500,000+ SKUs.</p>
        </div>
      </article>
      <article class="str-card reveal">
        <div class="str-card__img"><span class="str-card__num">02</span><img src="../assets/img/recruit-division-ict-hero.jpg" alt="Engineers building the parts compatibility search" loading="lazy"></div>
        <div class="str-card__body">
          <h3>Japan's first exact-match<br>parts compatibility search, built in-house</h3>
          <p>We were the first in the industry to build an open search that finds compatible parts by frame number, model code or OEM part number. It also supports OEM-number lookup and brand-wide search in one query. Powered by our own database — updated daily — it pinpoints the right item from hundreds of thousands.</p>
        </div>
      </article>
      <article class="str-card reveal">
        <div class="str-card__img"><span class="str-card__num">03</span><img src="../assets/img/strength-callcenter.jpg" alt="Customer center operator on the phone" loading="lazy"></div>
        <div class="str-card__body">
          <h3>A customer center staffed<br>by our own operators</h3>
          <p>To handle parts fitting per vehicle and selection from hundreds of thousands of items, we run our own customer center. Beyond web and fax, we take phone orders too. Conversations with customers surface industry issues early, and we feed them straight into our services and product development.</p>
        </div>
      </article>
      <article class="str-card reveal">
        <div class="str-card__img"><span class="str-card__num">04</span><img src="../assets/img/strength-qc.jpg" alt="Outbound inspection and quality control at a factory" loading="lazy"></div>
        <div class="str-card__body">
          <h3>Thorough quality control<br>by dedicated staff</h3>
          <p>Every item is inspected at inbound and outbound. Our development staff also travel to overseas factories in person to manage the production process and run shipment inspections on site — an uncompromising quality regime that delivers only safe, reliable products.</p>
        </div>
      </article>
      <article class="str-card reveal">
        <div class="str-card__img"><span class="str-card__num">05</span><img src="../assets/img/strength-logistics.jpg" alt="Logistics center storing hundreds of thousands of items" loading="lazy"></div>
        <div class="str-card__body">
          <h3>Logistics that ship hundreds of<br>thousands of items same-day</h3>
          <p>With logistics hubs in Japan and overseas, we control the entire flow — from the point of manufacture to the customer's hands, including storage and service — through our own systems. By optimizing the whole supply chain, we achieve same-day shipping of in-stock items.</p>
        </div>
      </article>
    </div>
    <div class="str-nav reveal" data-scroller="strengthsScroller">
      <button type="button" data-dir="prev" aria-label="Previous">‹</button>
      <button type="button" data-dir="next" aria-label="Next">›</button>
    </div>
    </div>
  </div>
</section>

<section class="brands" id="brands">
  <div class="inner">
    <p class="sec-label reveal">BRANDS</p>
    <h2 class="sec-title sec-title--light reveal">A house of brands.</h2>
    <p class="sec-lead sec-lead--light reveal">Original brands developed in-house, and world-class brands we represent as the exclusive distributor for Japan — two portfolios that expand the choices of professionals and riders.</p>
  </div>

  <a class="smart-feature reveal" href="brands.html" aria-label="SMART SERIES">
    <video class="smart-feature__video" src="../assets/video/smart-srd.mp4" autoplay muted loop playsinline></video>
    <div class="smart-feature__inner">
      <p class="smart-feature__tag">OUR BRAND — FOCUS</p>
      <h3 class="smart-feature__title">SMART SERIES</h3>
      <p class="smart-feature__copy">Smart riding, as standard equipment.<br>Displays, power, air and wash — gadgets that upgrade the touring experience.</p>
      <ul class="smart-feature__chips">
        <li>SRD 5 Smart Ride Display</li>
        <li>SmartCarLink</li>
        <li>SAP2000 Air Pump</li>
        <li>Smart Portable 01</li>
      </ul>
    </div>
  </a>

  <div class="brand-mosaic">
    <a class="brand-tile" href="https://exs.customjapan.net/" target="_blank" rel="noopener">
      <video src="../assets/video/brand-exs.mp4" autoplay muted loop playsinline></video>
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">OUR BRAND</span>
        <h3>eXs</h3>
        <p>Next-gen mobility that ran at EXPO 2025 — from e-scooters to e-bikes.</p>
      </div>
    </a>
    <a class="brand-tile" href="https://asmax.customjapan.net/" target="_blank" rel="noopener">
      <img src="../assets/img/ride-night.jpg" alt="ASMAX" loading="lazy">
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">PARTNER BRAND</span>
        <h3>ASMAX</h3>
        <p>Next-generation smart intercoms, exclusively distributed in Japan.</p>
      </div>
    </a>
    <a class="brand-tile" href="https://shad-japan.com/" target="_blank" rel="noopener">
      <video src="../assets/video/brand-shad.mp4" autoplay muted loop playsinline></video>
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">PARTNER BRAND</span>
        <h3>SHAD</h3>
        <p>World-standard motorcycle cases from Spain. Shad Bikes now in Japan.</p>
      </div>
    </a>
    <a class="brand-tile" href="https://sp-connect.customjapan.net/" target="_blank" rel="noopener">
      <img src="../assets/img/spconnect.jpg" alt="SP Connect" loading="lazy">
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">PARTNER BRAND</span>
        <h3>SP Connect</h3>
        <p>One smartphone for every ride. Official sales in Japan since 2026.</p>
      </div>
    </a>
    <a class="brand-tile" href="https://eleveit.customjapan.net/" target="_blank" rel="noopener">
      <img src="../assets/img/eleveit-enduro.jpg" alt="ELEVEIT" loading="lazy">
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">PARTNER BRAND</span>
        <h3>ELEVEIT</h3>
        <p>Italian off-road boots developed with world champion Steve Holcombe.</p>
      </div>
    </a>
    <a class="brand-tile" href="https://www.timsun-japan.com/" target="_blank" rel="noopener">
      <img src="../assets/img/slide-timsun2.jpg" alt="TIMSUN" loading="lazy">
      <div class="brand-tile__veil"></div>
      <div class="brand-tile__body">
        <span class="brand-tile__tag">PARTNER BRAND</span>
        <h3>TIMSUN</h3>
        <p>Tires running in 40+ countries. Official supporter of JNCC &amp; CGC.</p>
      </div>
    </a>
  </div>
</section>

<section class="brand-logos">
  <div class="inner">
    <div class="brands__group reveal" style="text-align:center">
      <a href="brands.html" class="btn-line">View all brands</a>
    </div>
  </div>
</section>

<section class="news" id="news">
  <div class="inner">
    <div class="news__head reveal">
      <div>
        <p class="sec-label">NEWS</p>
        <h2 class="sec-title">Latest news</h2>
      </div>
      <a href="news.html" class="btn-line">View all</a>
    </div>
    <ul class="news__list">
      <li class="reveal"><a href="https://note.com/fair_auk890/n/nc095a7961e8d" target="_blank" rel="noopener">
        <time>2026.06.16</time><span class="news__cat news__cat--info">INFO</span>
        <p>Over 20 straight years of revenue growth — we're hiring people to build that growth with us</p>
      </a></li>
      <li class="reveal"><a href="https://www.motomegane.com/car_news/pickup-car/customjapan-10_20260610" target="_blank" rel="noopener">
        <time>2026.06.13</time><span class="news__cat news__cat--media">MEDIA</span>
        <p>Automotive web magazine “Moto Megane CARS” features SmartCarLink</p>
      </a></li>
      <li class="reveal"><a href="https://www.customjapan.net/a/cycle/16781" target="_blank" rel="noopener">
        <time>2026.06.08</time><span class="news__cat news__cat--media">MEDIA</span>
        <p>Electric kickboard “eXs”, adopted at EXPO 2025, to appear on BS TV Tokyo's “Trend EYE”</p>
      </a></li>
      <li class="reveal"><a href="https://www.customjapan.net/a/car/15808" target="_blank" rel="noopener">
        <time>2026.05.01</time><span class="news__cat">PRODUCT</span>
        <p>“SmartCarLink” launches — turn your car navigation into a smartphone</p>
      </a></li>
      <li class="reveal"><a href="https://prtimes.jp/main/html/rd/p/000000083.000070755.html" target="_blank" rel="noopener">
        <time>2026.04.21</time><span class="news__cat">PRESS</span>
        <p>Japan premiere: SHAD's urban bicycle line “Shad Bikes” debuts</p>
      </a></li>
      <li class="reveal"><a href="https://www.customjapan.net/a/moto/14699" target="_blank" rel="noopener">
        <time>2026.04.07</time><span class="news__cat news__cat--event">EVENT</span>
        <p>Tokyo Motorcycle Show 2026 — after-report &amp; photo album</p>
      </a></li>
    </ul>
  </div>
</section>

<section class="recruit" id="recruit">
  <div class="recruit__bg"><img src="../assets/img/world-ride.jpg" alt=""></div>
  <div class="recruit__content inner">
    <p class="sec-label sec-label--light reveal">RECRUIT</p>
    <h2 class="recruit__title reveal">Join us in crafting<br>the future of riding.</h2>
    <p class="recruit__lead reveal">Product development, marketing, ICT and logistics — in Osaka, Japan.<br>(Recruiting site is in Japanese)</p>
    <a href="../recruit/index.html" class="btn-solid reveal">Careers (JP)</a>
  </div>
</section>

<section class="explore">
  <div class="inner">
    <p class="sec-label reveal">EXPLORE</p>
    <h2 class="sec-title sec-title--sm reveal">Get to know Custom Japan.</h2>
    <div class="explore__grid">
      <a href="about.html" class="explore-card reveal">
        <span class="explore-card__en">ABOUT</span>
        <h3>About us</h3>
        <p>Founded in 1954, with 70 years of history. Our philosophy, action guidelines and company profile — the foundation of Custom Japan.</p>
        <span class="explore-card__arrow" aria-hidden="true">&rarr;</span>
      </a>
      <a href="business.html" class="explore-card reveal">
        <span class="explore-card__en">BUSINESS</span>
        <h3>Business &amp; strengths</h3>
        <p>The platform that links makers worldwide with professional shops across Japan — and the five strengths behind it.</p>
        <span class="explore-card__arrow" aria-hidden="true">&rarr;</span>
      </a>
      <a href="brands.html" class="explore-card reveal">
        <span class="explore-card__en">BRANDS</span>
        <h3>Brands</h3>
        <p>Original brands we develop in-house, and the world-class brands we represent as the exclusive distributor for Japan.</p>
        <span class="explore-card__arrow" aria-hidden="true">&rarr;</span>
      </a>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- about
ABOUT_BODY = page_hero("ABOUT US", "COMPANY", "Philosophy, profile and history", "About") + """
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">PHILOSOPHY</p>
    <div class="philosophy reveal">
      <h2 class="philosophy__slogan">#ノル人をツクる</h2>
      <p class="philosophy__en">RIDE TOGETHER AND MOVE FORWARD</p>
      <p>Together with our colleagues, customers and partners, we connect parts with parts, knowledge with technology, and people with people — building the knowledge and distribution infrastructure that supports every professional in mobility.</p>
      <p>We grow with excitement and keep creating experiential value for our customers, going beyond the traditional wholesale function to nurture a platform where industry knowledge is shared and optimized, crafting a mobility culture for generations to come.</p>
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">GUIDELINE</p>
    <h2 class="sec-title sec-title--sm reveal">Our Guidelines</h2>
    <ol class="guideline reveal">
      <li>Work brightly, sincerely and with a positive mindset.</li>
      <li>Decide benefits based on numbers, facts and logic.</li>
      <li>Clarify objectives and drive a growth cycle of productivity.</li>
      <li>Speak short, simple and straight.</li>
      <li>Raise the quality of communication and share information effectively.</li>
      <li>Switch the subject — think and act from the other person's standpoint.</li>
    </ol>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">PROFILE</p>
    <h2 class="sec-title sec-title--sm reveal">Company Profile</h2>
    <table class="profile-table reveal">
      <tr><th>Company</th><td>Custom Japan Co., Ltd.</td></tr>
      <tr><th>Founded</th><td>August 9, 2005</td></tr>
      <tr><th>Capital</th><td>JPY 10,000,000</td></tr>
      <tr><th>Representative</th><td>Motoki Murai, President &amp; CEO</td></tr>
      <tr><th>Head office</th><td>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>TEL +81-6-6563-9317 / FAX +81-6-6634-8239</td></tr>
      <tr><th>Facilities</th><td>Logistics Center #1 (Higashiosaka, Osaka)<br>Logistics Center #2 (Yao, Osaka)</td></tr>
      <tr><th>Business</th><td>B2B sales of motorcycle, bicycle and automotive parts and tools / Parts supply for service shops nationwide / Import &amp; export of motor parts / Support for delivery businesses and franchises / Development of original brands</td></tr>
    </table>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">HISTORY</p>
    <h2 class="sec-title sec-title--sm reveal">Since 1954 — our distribution DNA</h2>
    <div class="timeline reveal">
      <div class="timeline__item"><div class="timeline__year">1954</div><div class="timeline__body"><h4>Tsuruhashi Buhin founded</h4><p>Yoshio Murai turns from bicycle repair to motorcycle parts wholesale in Higashinari-ku, Osaka.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2005</div><div class="timeline__body"><h4>Custom Japan Co., Ltd. established</h4><p>Founded in Tsuruhashi, Osaka as a venture-style business succession from Nihon Motor Parts. Original brands MIRAX, TORUNA and PFP launch; the first wholesale catalog starts as four Excel sheets sent to 500 bike shops.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2006</div><div class="timeline__body"><h4>ProTOOLs launched</h4><p>Professional tool brand for service shops.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2007</div><div class="timeline__body"><h4>ProSelect Battery launched</h4><p>Professional-grade motorcycle batteries.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2008</div><div class="timeline__body"><h4>Logistics center opens in Higashiosaka</h4><p>First exhibit at the Tokyo Motorcycle Show.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2016</div><div class="timeline__body"><h4>Catalog Vol.10 — 150,000 items</h4><p>Industry-leading scale; 200,000 items the following year.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2020</div><div class="timeline__body"><h4>Next-gen mobility brand "eXs" born</h4><p>Two e-scooter models launch simultaneously.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2023</div><div class="timeline__body"><h4>Official supplier of EXPO 2025 smart mobility</h4><p>The road-legal "eXs 1 TKG" tops Makuake crowdfunding records.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2024</div><div class="timeline__body"><h4>Exclusive distributor of ELEVEIT</h4><p>The Smart Series begins with the SRD 5 smart ride display.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2025</div><div class="timeline__body"><h4>20th anniversary</h4><p>Exclusive distribution of ASMAX begins; "eXs" supports operations at EXPO 2025 Osaka-Kansai.</p></div></div>
      <div class="timeline__item"><div class="timeline__year">2026</div><div class="timeline__body"><h4>SP Connect official sales begin</h4><p>Largest-ever booth at the Tokyo Motorcycle Show; first exhibit at the Suzuka 8 Hours.</p></div></div>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- business
BUSINESS_BODY = page_hero("BUSINESS", "PLATFORM", "The system that keeps professional procurement running", "Business") + """
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OVERVIEW</p>
    <h2 class="sec-title sec-title--sm reveal">Every part a pro needs,<br>on a single platform.</h2>
    <p class="sec-lead reveal">Between global manufacturers and 90,000 professional shops in Japan, Custom Japan handles inventory, logistics and data end to end. With a database of 500,000+ SKUs and same-day shipping, we keep professional workshops running.</p>
    <div class="business__flow reveal">
      <div class="flow-node"><em>Global makers<br>&amp; brands</em></div>
      <div class="flow-arrow"></div>
      <div class="flow-node flow-node--center"><strong>CUSTOM JAPAN</strong><em>Inventory / Logistics / Data / R&amp;D</em></div>
      <div class="flow-arrow"></div>
      <div class="flow-node"><em>90,000 pro shops<br>across Japan</em></div>
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">OUR STRENGTHS</p>
    <h2 class="sec-title sec-title--sm reveal">Five strengths of Custom Japan</h2>
    <div class="strengths">
      <div class="strength reveal"><span class="strength__num">01</span><h3>Industry-leading wholesale catalog,<br>print and members-only web</h3><p>A print catalog covering essential maintenance parts, combined with a closed, members-only web catalog. Filtering and comparison tools guide pros through 500,000+ SKUs.</p></div>
      <div class="strength reveal"><span class="strength__num">02</span><h3>Japan's first exact-match<br>parts compatibility search</h3><p>Search compatible parts by frame number, model code or OEM part number — powered by our own database, updated daily.</p></div>
      <div class="strength reveal"><span class="strength__num">03</span><h3>A customer center staffed<br>by our own operators</h3><p>Phone-based support for parts fitting and selection, alongside web and fax ordering. Voices from the field feed directly into our services and product development.</p></div>
      <div class="strength reveal"><span class="strength__num">04</span><h3>Thorough quality control<br>by dedicated staff</h3><p>Inspection at every inbound and outbound step, plus direct process management at overseas factories by our development team.</p></div>
      <div class="strength reveal"><span class="strength__num">05</span><h3>Logistics that ship hundreds of<br>thousands of items same-day</h3><p>Domestic and overseas logistics hubs controlled by our own systems — same-day shipping for in-stock orders placed by 4 p.m.</p></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OUR SERVICES</p>
    <h2 class="sec-title sec-title--sm reveal">Our platforms</h2>
    <div class="site-cards">
      <a class="site-card reveal" href="https://www.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">B2B PLATFORM</span><h3>Custom Japan Wholesale Catalog</h3><p>Members-only wholesale platform for motorcycle, bicycle and automotive parts, accessories and tools.</p><span class="site-card__url">customjapan.net</span></a>
      <a class="site-card reveal" href="https://moto.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">MOTORCYCLE</span><h3>Moto Custom</h3><p>Motorcycle parts and accessories with model-fit search.</p><span class="site-card__url">moto.customjapan.net</span></a>
      <a class="site-card reveal" href="https://cycle.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">BICYCLE</span><h3>Cycle Custom</h3><p>Bicycle parts and accessories, from city rides to sport cycling.</p><span class="site-card__url">cycle.customjapan.net</span></a>
      <a class="site-card reveal" href="https://car.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">CAR</span><h3>Car Custom</h3><p>Automotive parts, accessories and smart gadgets.</p><span class="site-card__url">car.customjapan.net</span></a>
      <a class="site-card reveal" href="https://tool.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">TOOL</span><h3>Tool Custom</h3><p>Maintenance tools and garage equipment, including ProTOOLs.</p><span class="site-card__url">tool.customjapan.net</span></a>
      <a class="site-card reveal" href="https://exs.customjapan.net/" target="_blank" rel="noopener"><span class="site-card__tag">BRAND SITE</span><h3>eXs Official Site</h3><p>Official site of our next-generation mobility brand.</p><span class="site-card__url">exs.customjapan.net</span></a>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- brands
BRAND_URLS = {'eXs': 'https://exs.customjapan.net/', 'ProSelect Battery': 'https://www.proselect.jp/', 'ProTOOLs': 'https://protools.customjapan.jp/', 'MIRAX': 'https://mirax.customjapan.jp/', 'moto boite BB': 'https://motoboite.customjapan.jp/', 'Optimum': 'https://optimum.customjapan.jp/', 'KUSTOM1': 'https://moto.customjapan.net/search?q=KUSTOM1', 'PFP': 'https://pfp.customjapan.jp/', 'TORUNA': 'https://toruna.customjapan.jp/', 'Re:code': 'https://moto.customjapan.net/search?q=Re%3Acode', 'ROLZ': 'https://moto.customjapan.net/search?q=ROLZ', 'Smart Arms': 'https://moto.customjapan.net/search?q=Smart+Arms', 'ASMAX': 'https://asmax.customjapan.net/', 'SHAD': 'https://shad-japan.com/', 'TIMSUN': 'https://www.timsun-japan.com/', 'ZONTES': 'https://moto.customjapan.net/search?filter-maker=5&maker=5', 'ELEVEIT': 'https://eleveit.customjapan.net/', 'ariete': 'https://www.ariete.com/', 'UFO PLAST': 'https://us.ufoplast.com/', 'PROTAPER': 'https://moto.customjapan.net/search?q=PROTAPER', 'CUSTOM CHROME': 'https://www.customchrome.com/', 'TORCH': 'https://torchsparkplug.japanese.globalmarket.com/', 'AIRACE': 'https://airace-japan.com/', 'TOBE': 'https://moto.customjapan.net/search?q=TOBE', 'NCY': 'https://www.ncy-motor.com.tw/', 'JETECH TOOL': 'https://www.jetech-japan.com/', 'COMPASS': 'https://www.customjapan.net/maker/COMPASS', 'IXIL': 'https://www.customjapan.net/maker/IXIL', 'Polisport': 'https://www.polisport.com/en/', 'UNIBEAR': 'https://moto.customjapan.net/search?q=UNIBEAR', 'SP Connect': 'https://sp-connect.customjapan.net/'}


def brand_card(logo, name, desc):
    url = BRAND_URLS[name]
    return (
        f'<a class="brand-card reveal" href="{url}" target="_blank" rel="noopener">'
        f'<div class="brand-card__logo">'
        f'<img src="../assets/brands/{logo}" alt="{name}"></div>'
        f"<h3>{name}</h3><p>{desc}</p></a>"
    )


OUR_BRANDS = [
    ("pic_brand_original_eXs.png", "eXs", "Next-generation mobility that ran at EXPO 2025 — from e-scooters to e-bikes."),
    ("pic_brand_original_proselect_bk.png", "ProSelect Battery", "Professional-grade motorcycle batteries since 2007."),
    ("pic_brand_original_protools.png", "ProTOOLs", "Tools and chemicals for professional workshops, now including portable power."),
    ("pic_brand_original_mirax.png", "MIRAX", "Motorcycle mirrors — a basics brand from our founding days."),
    ("pic_brand_original_bb.png", "moto boite BB", "Boxes and storage that create space for motorcycles."),
    ("pic_brand_original_optimum.png", "Optimum", "Parts and accessories balancing cost and quality for riders."),
    ("pic_brand_original_kustomone.png", "KUSTOM1", "Parts for the custom scene."),
    ("pic_brand_original_pfp.png", "PFP", "OEM-compatible replacement parts, including front fork inner tubes."),
    ("pic_brand_original_toruna.png", "TORUNA", "Comprehensive anti-theft and security products."),
    ("pic_brand_original_recode.png", "Re:code", "Renewal solutions for mobility parts."),
    ("pic_brand_original_rolz.png", "ROLZ", "Parts and accessories supporting everyday riding."),
    ("pic_brand_original_Smart_Arms.png", "Smart Arms", "Mounts and arms for smart devices."),
]

PARTNER_BRANDS = [
    ("pic_brand_abroad_asmax.png", "ASMAX", "Voice-controlled next-gen smart intercoms; exclusive distributor for Japan. The EVA RACING collab model is a hot topic."),
    ("pic_brand_abroad_shad.png", "SHAD", "World-standard motorcycle cases from Spain; Shad Bikes urban line now in Japan."),
    ("pic_brand_abroad_timsun.png", "TIMSUN", "Tires running in 40+ countries; official supporter of JNCC and CGC hard enduro."),
    ("pic_brand_abroad_zontes.png", "ZONTES", "A fast-rising motorcycle brand in Europe."),
    ("pic_brand_abroad_eleveit.png", "ELEVEIT", "Italian off-road boots developed with world champion Steve Holcombe."),
    ("pic_brand_abroad_ariete.png", "ariete", "Italian goggles and grips, including 8K goggles."),
    ("pic_brand_abroad_ufoplast.png", "UFO PLAST", "Italian off-road plastics and protection."),
    ("pic_brand_abroad_protaper.png", "PROTAPER", "US off-road components, best known for handlebars."),
    ("pic_brand_abroad_customchrome.png", "CUSTOM CHROME", "The global brand for Harley-Davidson custom parts."),
    ("pic_brand_abroad_torch.png", "TORCH", "Spark plugs distributed worldwide."),
    ("pic_brand_abroad_airace.png", "AIRACE", "Bicycle pumps and inflation specialists."),
    ("pic_brand_abroad_tobe.png", "TOBE", "Riding gear built for harsh environments."),
    ("pic_brand_abroad_ncy.png", "NCY", "Scooter custom parts."),
    ("pic_brand_abroad_jetechtool.png", "JETECH TOOL", "Maintenance tools for professional use."),
    ("pic_brand_abroad_compass_2021.png", "COMPASS", "Mobility parts and accessories."),
    ("pic_brand_abroad_ixil.png", "IXIL", "Exhaust systems from Spain."),
    ("pic_brand_abroad_polisport.png", "Polisport", "Portuguese plastics, handguards and child seats."),
    ("pic_brand_abroad_unibear.png", "UNIBEAR", "Drive chain specialists."),
]

BRANDS_BODY = page_hero("BRANDS", "PORTFOLIO", "Original brands and world brands — two portfolios", "Brands") + f"""
<section class="page-section" style="padding-bottom:0">
  <div class="inner">
    <p class="sec-label reveal">FOCUS</p>
    <h2 class="sec-title sec-title--sm reveal">Smart Series — smart riding for everyone.</h2>
    <p class="sec-lead reveal">The CarPlay/Android Auto-ready SRD 5 display, SmartCarLink which turns OEM car navigation into a smartphone hub, the SAP2000 electric air pump, and the cord-free Smart Portable 01 washer — in-house gadgets that upgrade touring and garage life.</p>
  </div>
  <a class="smart-feature reveal" href="https://car.customjapan.net/" target="_blank" rel="noopener" aria-label="SMART SERIES">
    <video class="smart-feature__video" src="../assets/video/smart-srd.mp4" autoplay muted loop playsinline></video>
    <div class="smart-feature__inner">
      <p class="smart-feature__tag">OUR BRAND — FOCUS</p>
      <h3 class="smart-feature__title">SMART SERIES</h3>
      <p class="smart-feature__copy">Displays, power, air and wash.<br>Updating the whole riding experience.</p>
      <ul class="smart-feature__chips">
        <li>SRD 5 Smart Ride Display</li>
        <li>SmartCarLink</li>
        <li>SAP2000 Air Pump</li>
        <li>Smart Portable 01</li>
      </ul>
    </div>
  </a>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OUR BRANDS</p>
    <h2 class="sec-title sec-title--sm reveal">Original brands</h2>
    <div class="brand-list">
      {''.join(brand_card(*b) for b in OUR_BRANDS)}
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">PARTNER BRANDS</p>
    <h2 class="sec-title sec-title--sm reveal">Exclusive &amp; authorized distribution</h2>
    <div class="brand-list">
      {''.join(brand_card(*b) for b in PARTNER_BRANDS)}
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- events
EVENTS_BODY = page_hero("EVENTS &amp; RACING", "ON THE SCENE", "Shows, races and EXPO — where we meet the ride", "Events") + """
<style>
.events-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:26px}
.events-grid .event-card{flex:none}
@media(max-width:768px){.events-grid{grid-template-columns:1fr}}
.event-card__links{padding:0 26px 24px;display:flex;gap:16px;flex-wrap:wrap}
.event-card__links a{font-family:var(--font-en);font-weight:600;font-size:11px;letter-spacing:.14em;color:var(--c-blue);border-bottom:1px solid currentColor;padding-bottom:2px}
</style>
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">2026 ACTIVITIES</p>
    <h2 class="sec-title sec-title--sm reveal">Exhibitions &amp; racing</h2>
    <div class="events-grid">
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/ride-night.jpg" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat event-card__cat--race">RACE</span><time>JUL 3–5, 2026 · Suzuka Circuit</time></div>
          <h3>"Coca-Cola" Suzuka 8 Hours Endurance Race</h3>
          <p>We made our first exhibit at Japan's biggest motorcycle race. Inside the Nankai Village booth we showed ASMAX smart intercoms, SHAD's TERRA series and SH38X, the SRD 5 smart ride display and the Smart Series gadgets. A report is coming soon.</p>
        </div>
      </article>
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/eleveit-enduro.jpg" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat event-card__cat--race">RACE</span><time>SEASON 2026</time></div>
          <h3>JEC All-Japan Enduro / JNCC / CGC</h3>
          <p>As the exclusive distributor of ELEVEIT and official tire supporter through TIMSUN, we back Japan's top off-road racing categories.</p>
        </div>
      </article>
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/event-tmcs2026.jpg" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat">SHOW</span><time>MAR 2026 · Tokyo Big Sight</time></div>
          <h3>53rd Tokyo Motorcycle Show 2026</h3>
          <p>Celebrating our 20th anniversary with our largest booth ever — a three-brand lineup of TIMSUN, SHAD and Custom Japan.</p>
        </div>
      </article>
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/event-omcs2026.png" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat">SHOW</span><time>MAR 2026 · Intex Osaka</time></div>
          <h3>42nd Osaka Motorcycle Show 2026</h3>
          <p>Featuring the ASMAX "EVA R" (Evangelion Racing) model and the Smart Series, with visitor-participation events.</p>
        </div>
      </article>
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/event-cyclemode.webp" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat">SHOW</span><time>FEB–APR 2026 · Tokyo / Osaka</time></div>
          <h3>Cycle Mode Tokyo / Osaka 2026</h3>
          <p>Our next-gen mobility brand "eXs" debuted at Japan's largest sports cycling festivals, with test rides at Expo '70 Park and the Japan premiere of Shad Bikes.</p>
        </div>
      </article>
      <article class="event-card reveal">
        <div class="event-card__img"><img src="../assets/img/exs-street-ride.jpg" alt="" loading="lazy"></div>
        <div class="event-card__body">
          <div class="event-card__meta"><span class="event-card__cat event-card__cat--expo">EXPO</span><time>2025 · Osaka, Kansai</time></div>
          <h3>EXPO 2025 Osaka-Kansai — Official Supplier</h3>
          <p>As a smart mobility supplier, "eXs" supported smooth venue operations — last-mile mobility running in the real world.</p>
        </div>
      </article>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- news
NEWS_ITEMS = [
    ("2026.06.30", "PRESS", "Official Japanese sales of SP Connect begin — one smartphone for every ride", "000000088"),
    ("2026.05.01", "PRESS", "SmartCarLink launches: turn OEM car navigation into your smartphone, leaving no personal data in the car", "000000084"),
    ("2026.04.20", "PRESS", "Japan premiere: SHAD's urban bicycle line “Shad Bikes” debuts at Cycle Mode Tokyo 2026", "000000083"),
    ("2026.04.17", "EVENT", "Next-gen mobility brand eXs debuts at Cycle Mode Tokyo 2026", "000000082"),
    ("2026.03.11", "EVENT", "Tokyo Motorcycle Show 2026: our largest booth ever for the 20th anniversary", "000000077"),
    ("2026.03.06", "EVENT", "Osaka Motorcycle Show 2026: ASMAX EVA R model and the Smart Series on display", "000000076"),
    ("2026.02.20", "SERVICE", "Same-day shipping cutoff extended to 4 p.m.", "000000075"),
    ("2025.11.01", "PRESS", "ASMAX × EVA RACING smart intercom “EVA R model” released", "000000071"),
    ("2025.10.02", "PRESS", "Smart Portable series begins with a cord-free rechargeable pressure washer", "000000070"),
    ("2025.09.29", "PRESS", "Next-gen smart intercom ASMAX S2 lands in Japan", "000000069"),
    ("2025.08.29", "PRESS", "ASMAX F1 Pro intercom makes its Japan debut", "000000067"),
    ("2025.08.08", "INFO", "Custom Japan celebrates its 20th anniversary", "000000065"),
    ("2025.06.25", "PRESS", "e-bike “eXs Street” launches from EXPO 2025 partner brand eXs", "000000061"),
    ("2025.03.14", "EVENT", "eXs supports smooth venue operations at EXPO 2025 Osaka-Kansai", "000000056"),
]

NEWS_EN_LIST = (Path(__file__).resolve().parent / "news_en_list.html").read_text(encoding="utf-8")
NEWS_EN_COUNT = NEWS_EN_LIST.count("<li ")
NEWS_BODY = page_hero("NEWS", "TOPICS", "News, press releases and media coverage", "News") + f"""
<section class="page-section">
  <div class="inner">
    <div class="news__head reveal">
      <div>
        <p class="sec-label">ALL TOPICS</p>
        <h2 class="sec-title sec-title--sm">News archive</h2>
      </div>
    </div>
    <div class="news-filter reveal" id="newsFilter">
      <button class="is-active" data-filter="all">All</button>
      <button data-filter="info">News</button>
      <button data-filter="press">Press releases</button>
      <button data-filter="media">Media</button>
      <span class="news-filter__count" id="newsCount"></span>
    </div>
    <ul class="news__list" id="newsList">
{NEWS_EN_LIST}
    </ul>
    <p style="margin-top:36px;font-size:12px;color:var(--c-gray)">* An archive of {NEWS_EN_COUNT} items — news, media coverage and press releases. Each item links to the source (PR TIMES, the original media outlet or our own sites); some sources are in Japanese.</p>
  </div>
</section>
<script>
(function(){{
  var f=document.getElementById('newsFilter'), list=document.getElementById('newsList'), cnt=document.getElementById('newsCount');
  var items=[].slice.call(list.querySelectorAll('li'));
  function apply(cat){{var n=0;items.forEach(function(li){{var s=cat==='all'||li.getAttribute('data-cat')===cat;li.hidden=!s;if(s)n++;}});cnt.textContent=n+' items';}}
  f.addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;f.querySelectorAll('button').forEach(function(x){{x.classList.remove('is-active');}});b.classList.add('is-active');apply(b.getAttribute('data-filter'));}});
  apply('all');
}})();
</script>"""

# ---------------------------------------------------------------- contact
CONTACT_BODY = page_hero("CONTACT", "GET IN TOUCH", "Business, support and media inquiries", "Contact") + """
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">CONTACT</p>
    <h2 class="sec-title sec-title--sm reveal">Choose the right channel</h2>
    <div class="contact-cards">
      <div class="contact-card reveal">
        <h3>Dealers &amp; shops — new business</h3>
        <p>We operate a members-only wholesale platform for motorcycle, bicycle and automotive dealers and service shops in Japan. Registration is free (Japanese site).</p>
        <a href="https://www.customjapan.net/" target="_blank" rel="noopener" class="btn-solid" style="text-align:center">Wholesale membership (JP)</a>
      </div>
      <div class="contact-card reveal">
        <h3>Brands &amp; manufacturers — distribution</h3>
        <p>Interested in entering the Japanese market? As the exclusive distributor for brands like ASMAX, SHAD and SP Connect, we handle import, marketing and nationwide B2B distribution.<br><br>E-mail info@customjapan.jp</p>
      </div>
      <div class="contact-card reveal">
        <h3>Media &amp; other inquiries</h3>
        <p>For press coverage, brand collaborations and everything else, please reach us by e-mail.<br><br>E-mail info@customjapan.jp<br>TEL +81-6-6563-9317</p>
        <a href="https://prtimes.jp/main/html/searchrlp/company_id/70755" target="_blank" rel="noopener" class="btn-line" style="text-align:center">Press releases (JP)</a>
      </div>
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">ACCESS</p>
    <h2 class="sec-title sec-title--sm reveal">Locations</h2>
    <table class="profile-table reveal">
      <tr><th>Head office</th><td>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>TEL +81-6-6563-9317</td></tr>
      <tr><th>Logistics Center #1</th><td>9-5 Minami-Kamikosaka, Higashiosaka, Osaka 577-0814, Japan</td></tr>
      <tr><th>Logistics Center #2</th><td>2-15 Minami-Kinomoto, Yao, Osaka 581-0042, Japan</td></tr>
    </table>
  </div>
</section>"""

PAGES = {
    "index.html": ("Custom Japan Co., Ltd. | Mobility Aftermarket Platform Company", "Custom Japan is a B2B distribution platform company from Osaka, delivering parts for motorcycles, bicycles and automobiles to 90,000 professional shops across Japan.", INDEX_BODY, False, True),
    "about.html": ("About | Custom Japan Co., Ltd.", "Philosophy, company profile and history of Custom Japan — distribution roots since 1954.", ABOUT_BODY, True, False),
    "business.html": ("Business | Custom Japan Co., Ltd.", "Custom Japan's B2B platform: 500,000+ SKUs, exact-match parts search and same-day logistics.", BUSINESS_BODY, True, False),
    "brands.html": ("Brands | Custom Japan Co., Ltd.", "Original brands including the Smart Series and eXs, plus exclusive distribution of ASMAX, SHAD, TIMSUN, SP Connect and more.", BRANDS_BODY, True, False),
    "events.html": ("Events & Racing | Custom Japan Co., Ltd.", "Suzuka 8 Hours, Tokyo & Osaka Motorcycle Shows, Cycle Mode, JEC/JNCC sponsorship and EXPO 2025 activities.", EVENTS_BODY, True, False),
    "news.html": ("News | Custom Japan Co., Ltd.", "Latest press releases and announcements from Custom Japan.", NEWS_BODY, True, False),
    "contact.html": ("Contact | Custom Japan Co., Ltd.", "Business, distribution and media inquiries for Custom Japan Co., Ltd.", CONTACT_BODY, True, False),
}

for page, (title, desc, body, solid, loader) in PAGES.items():
    html = chrome(page, title, desc, body, header_solid=solid, with_loader=loader)
    (OUT / page).write_text(html, encoding="utf-8")
    print("wrote", OUT / page)
