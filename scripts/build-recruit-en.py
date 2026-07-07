#!/usr/bin/env python3
"""採用サイトの英語版(recruit/en/*)を生成する。
CSSはJP版 recruit/index.html から抽出して再利用。英語の本文・データ・スクリプトのみ保持。
使い方: python3 scripts/build-recruit-en.py"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JP_INDEX = (ROOT / "recruit" / "index.html").read_text(encoding="utf-8")
CSS = re.search(r"<style>.*?</style>", JP_INDEX, re.S).group(0)  # index用インラインCSS(言語非依存)
OUT = ROOT / "recruit" / "en"
(OUT / "division").mkdir(parents=True, exist_ok=True)
BASE = "https://customjapan.jp"

# ---- SEO head ----
def seo(path, title, desc, ja_path):
    url = BASE + "/recruit/en/" + path
    ja = BASE + "/recruit/" + ja_path
    return f'''<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Custom Japan Co., Ltd.">
<meta property="og:locale" content="en_US"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/recruit-work-catalog.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="ja" href="{ja}"><link rel="alternate" hreflang="en" href="{url}"><link rel="alternate" hreflang="x-default" href="{ja}">'''

# ================= INDEX =================
NAV = [("#values","VALUES"),("#jobs","JOBS"),("#people","PEOPLE"),("#benefits","BENEFITS"),("#flow","FLOW"),("#faq","FAQ")]
def nav_html():
    return "\n".join(f'    <a href="{h}">{t}</a>' for h,t in NAV)

INDEX_HEAD = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Careers | Custom Japan Co., Ltd. RECRUIT</title>
<meta name="description" content="Careers at Custom Japan. 125 days off a year and ~1.2h/day average overtime — a genuinely workable environment where you help build the future of mobility. Mid-career & new-grad hiring, employee interviews and benefits.">
<link rel="icon" href="../../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/style.css">
{CSS}
{seo("index.html","Careers | Custom Japan Co., Ltd.","Careers at Custom Japan — build the future of mobility.","index.html")}
</head>
<body>

<header class="header header--solid" id="header">
  <a href="index.html" class="header__logo">
    <img src="../../assets/logo/cj-logo-white-text.svg" alt="" class="header__logo-white" aria-hidden="true">
    <img src="../../assets/logo/cj-logo-black-text.svg" alt="Custom Japan Co., Ltd." class="header__logo-color">
  </a>
  <nav class="header__nav">
{nav_html()}
    <a href="global.html" class="header__lang">Global Talent</a>
    <a href="../index.html" class="header__lang">日本語</a>
    <a href="#entry" class="header__recruit"><span class="header__recruit-en">ENTRY</span><span class="header__recruit-jp">Apply</span></a>
  </nav>
  <button class="header__menu-btn" id="menuBtn" aria-controls="mobileMenu" aria-expanded="false" aria-label="Menu"><span></span><span></span></button>
</header>
<div class="mobile-menu" id="mobileMenu">
  <nav>
{nav_html()}
    <a href="global.html">Global Talent</a>
    <a href="../index.html">日本語</a>
    <a href="#entry" class="mobile-menu__recruit">ENTRY — Apply</a>
  </nav>
</div>
<button class="mascot-top" id="mascotTop" aria-label="Back to top"><img src="../../assets/logo/cj-mascot.svg" alt=""><span>TOP</span></button>
<main>'''

INDEX_BODY = '''
<!-- HERO -->
<section class="rc-hero">
  <img src="../../assets/img/recruit-hero-team-generated.jpg" alt="" class="rc-hero__bg">
  <div class="rc-hero__inner">
    <p class="rc-hero__label">CUSTOM JAPAN RECRUITING</p>
    <h1 class="rc-hero__title">Your next career,<br>on the side that creates riders.</h1>
    <p class="rc-hero__lead">20 years in business, 107 employees. A company that takes on the future of mobility<br class="pc">while seriously building a genuinely workable environment.</p>
    <div class="rc-hero__btns">
      <a href="#positions" class="btn-solid">View open positions</a>
      <a href="#entry" class="btn-line btn-line--light">Apply</a>
    </div>
  </div>
  <div class="rc-strip" aria-label="Workplace data">
    <div><b>125<small>days</small></b><span>Annual holidays</span></div>
    <div><b>1.2<small>h/day</small></b><span>Avg. overtime</span></div>
    <div><b>4.9 : 5.1</b><span>Gender ratio</span></div>
    <div><b>7.25<small>yrs</small></b><span>Avg. tenure</span></div>
  </div>
</section>
<div class="crumb"><a href="../../en/index.html">Corporate</a><span>/</span>Careers</div>

<!-- DATA -->
<section class="page-section" id="data">
  <div class="inner">
    <p class="sec-label reveal">DATA</p>
    <h2 class="sec-title sec-title--sm reveal">The workplace, in numbers</h2>
    <p class="sec-lead reveal">"Workability" is best shown in numbers. We invest in holidays, lower overtime and DX as the foundation that supports challenge.</p>
    <div class="rc-data-grid reveal">
      <div class="rc-data"><b>125<small>days</small></b><h3>Annual holidays</h3><p>120 days off + 5 planned paid days. Paid leave taken proactively.</p></div>
      <div class="rc-data"><b>1.2<small>h/day</small></b><h3>Average overtime</h3><p>A focused way of working that protects work-life balance.</p></div>
      <div class="rc-data"><b>4.9 : 5.1</b><h3>Gender ratio</h3><p>A workplace where everyone thrives regardless of gender or age.</p></div>
      <div class="rc-data"><b>7.25<small>yrs</small></b><h3>Average tenure</h3><p>We keep building an environment where people stay and grow.</p></div>
      <div class="rc-data"><b>107</b><h3>Employees</h3><p>As of Sep 2025. A multinational team is active here.</p></div>
      <div class="rc-data"><b>850<small>k</small></b><h3>SKUs handled</h3><p>130k EC members. One of the industry's largest platforms.</p></div>
    </div>
  </div>
</section>

<!-- MESSAGE -->
<section class="page-section page-section--off" id="message">
  <div class="inner">
    <p class="sec-label reveal">MESSAGE</p>
    <h2 class="sec-title sec-title--sm reveal">Message from the CEO</h2>
    <div class="rc-message reveal">
      <div class="rc-message__photo">
        <img src="../../assets/img/president.jpg" alt="President & CEO, Motoki Murai" loading="lazy">
        <blockquote>Let's build the future together — valuing both challenge and security.</blockquote>
      </div>
      <div>
        <p style="font-size:13.5px;color:#3c4149;line-height:2.1">Our philosophy "Ride together, move forward" holds two ideas: enriching people's lives through mobility, and walking in the same direction as our customers and colleagues. Inheriting a family business of over half a century while launching a new venture — that "venture-style business succession" is our origin. You don't need to know much about vehicles when you join. Touching many kinds of work and naturally aligning with our philosophy — that growth process is the real reward of working here.</p>
        <p class="sig">President &amp; CEO <b>Motoki Murai</b></p>
      </div>
    </div>
  </div>
</section>

<!-- VALUES -->
<section class="page-section" id="values">
  <div class="inner">
    <p class="sec-label reveal">VALUES</p>
    <h2 class="sec-title sec-title--sm reveal">The people we want to work with</h2>
    <p class="sec-lead reveal">More than special skills, we value attitude. These are the qualities we look for, drawn from our action guidelines. You don't need mobility knowledge when you join.</p>
    <div class="value-grid">
      <div class="value-card reveal"><b>01</b><div><h3>Bright, sincere, positive-minded</h3><p>We take on many challenges without clear answers. We want people who find difficulty interesting and take the first step forward.</p></div></div>
      <div class="value-card reveal"><b>02</b><div><h3>Think in numbers, facts and logic</h3><p>Not just instinct — we welcome people who can explain "why" based on facts and data.</p></div></div>
      <div class="value-card reveal"><b>03</b><div><h3>Act from the other person's view</h3><p>Switch the subject from yourself to others. Think and act from the standpoint of customers, colleagues and partners.</p></div></div>
      <div class="value-card reveal"><b>04</b><div><h3>Curious about products and the world</h3><p>Vehicles, gadgets, overseas — if you keep learning with curiosity, experience is not required.</p></div></div>
    </div>
  </div>
</section>

<!-- JOBS / DIVISIONS -->
<section class="page-section page-section--off" id="jobs">
  <div class="inner">
    <p class="sec-label reveal">DIVISIONS</p>
    <h2 class="sec-title sec-title--sm reveal">Our work — six divisions</h2>
    <p class="sec-lead reveal">Because we go beyond a parts wholesaler and own "planning through sales," the range of roles is wide. Divisions tagged <span style="color:var(--c-red);font-weight:700">GLOBAL</span> trade heavily overseas, with a multinational team.</p>
    <div class="job-list">
      <a class="job-item reveal" href="division/product.html"><h3><span class="tag-global">GLOBAL</span>Product Development</h3><p>Next-gen mobility development, overseas & domestic buying. The heart that finds products worldwide and creates hits in Japan.</p></a>
      <a class="job-item reveal" href="division/global.html"><h3><span class="tag-global">GLOBAL</span>Global Business</h3><p>Across ASEAN, China and Taiwan — from dealer development to cross-border EC. Shaping business in markets without a set answer.</p></a>
      <a class="job-item reveal" href="division/marketing.html"><h3><span>MKT</span>Marketing</h3><p>Running EC sites, marketplaces and print catalogs — moving toward data-driven marketing with BI & MA tools.</p></a>
      <a class="job-item reveal" href="division/ict.html"><h3><span>ENG</span>ICT & Engineering</h3><p>In-house development of one of the world's largest bike-fitment DBs and a headless EC. Cutting-edge engineering in a legacy industry.</p></a>
      <a class="job-item reveal" href="division/scm.html"><h3><span>SCM</span>SCM & Fulfillment</h3><p>The logistics heart behind same-day shipping. Voices from the floor become company-wide systems.</p></a>
      <a class="job-item reveal" href="division/corporate.html"><h3><span>CORP</span>Corporate</h3><p>Accounting, general affairs, HR. Build the foundation of a growing company — from the systems up.</p></a>
    </div>
  </div>
</section>

<!-- BRANDS (full-bleed) -->
<section class="rc-brands">
  <div class="inner">
    <p class="sec-label reveal" style="color:#ff6b6a">OUR BRANDS</p>
    <h2 class="sec-title sec-title--sm reveal">The brands you'll move.</h2>
    <p class="rc-brands__lead reveal">Going beyond a parts wholesaler to own "planning through sales," we have both brands we created ourselves and brands we hold from around the world. After joining, in planning, buying, marketing and logistics, you'll work with these real brands — delivering both product and culture to the market with your own hands.</p>
    <div class="rc-brand-block reveal">
      <p class="rc-brand-cat"><span>Our own brands</span>Planned from zero, put to the market</p>
      <ul class="rc-brand-logos">
        <li><img src="../../assets/brands/pic_brand_original_eXs.png" alt="eXs"></li>
        <li><img src="../../assets/brands/pic_brand_original_protools.png" alt="ProTOOLs"></li>
        <li><img src="../../assets/brands/pic_brand_original_proselect_bk.png" alt="ProSelect"></li>
        <li><img src="../../assets/brands/pic_brand_original_mirax.png" alt="MIRAX"></li>
        <li><img src="../../assets/brands/pic_brand_original_optimum.png" alt="Optimum"></li>
        <li><img src="../../assets/brands/pic_brand_original_pfp.png" alt="PFP"></li>
      </ul>
    </div>
    <div class="rc-brand-block reveal">
      <p class="rc-brand-cat"><span>Exclusive / authorized distribution</span>Bringing the world's brands to Japan</p>
      <ul class="rc-brand-logos">
        <li><img src="../../assets/brands/pic_brand_abroad_asmax.png" alt="ASMAX"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_shad.png" alt="SHAD"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_timsun.png" alt="TIMSUN"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_zontes.png" alt="ZONTES"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_eleveit.png" alt="ELEVEIT"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_ariete.png" alt="ariete"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_customchrome.png" alt="CUSTOM CHROME"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_protaper.png" alt="PROTAPER"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_ufoplast.png" alt="UFO PLAST"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_polisport.png" alt="Polisport"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_ncy.png" alt="NCY"></li>
        <li><img src="../../assets/brands/pic_brand_abroad_torch.png" alt="TORCH"></li>
      </ul>
    </div>
    <div class="rc-brand-note reveal">
      <div><b>30<small>+</small></b><span>Brands handled</span></div>
      <div><b>850<small>k</small></b><span>SKUs handled</span></div>
      <div><b>7<small>countries</small></b><span>Overseas trade (ASEAN & Greater China)</span></div>
    </div>
  </div>
</section>

<!-- CULTURE -->
<section class="page-section" id="culture">
  <div class="inner">
    <p class="sec-label reveal">CULTURE</p>
    <h2 class="sec-title sec-title--sm reveal">Environment & culture</h2>
    <p class="sec-lead reveal">Challenge and security, together. A team of diverse backgrounds exchanges opinions on a flat footing, in an environment where people work for the long term.</p>
    <div class="culture-grid">
      <div class="culture-photos reveal">
        <img src="../../assets/img/recruit-office-1.jpg" alt="" loading="lazy">
        <img src="../../assets/img/recruit-office-2.jpg" alt="" loading="lazy">
        <img src="../../assets/img/recruit-culture-team-generated.jpg" alt="" loading="lazy">
        <img src="../../assets/img/recruit-entrance.jpg" alt="" loading="lazy">
      </div>
      <div class="culture-points reveal">
        <div class="culture-point"><b>4.9 : 5.1</b><span>A gender ratio where everyone thrives — regardless of role or nationality.</span></div>
        <div class="culture-point"><b>Multinational</b><span>Members from many countries, centered on product development and global business.</span></div>
        <div class="culture-point"><b>7.25<small>yrs</small></b><span>Average tenure. A base to work long and grow.</span></div>
        <div class="culture-point"><b>20<small>yrs</small></b><span>Consecutive revenue growth — a stable base to take on new challenges.</span></div>
      </div>
    </div>
  </div>
</section>

<!-- PEOPLE -->
<section class="page-section page-section--off" id="people">
  <div class="inner">
    <p class="sec-label reveal">PEOPLE</p>
    <h2 class="sec-title sec-title--sm reveal">Meet the people</h2>
    <p class="sec-lead reveal">Mid-career hires, part-timers promoted to full-time, career-changers from scratch. Read the real voices of seven people who joined through different doors — right here on this page.</p>
    <div class="people-grid reveal" id="peopleGrid"></div>
  </div>
</section>

<!-- GROWTH -->
<section class="page-section" id="growth">
  <div class="inner">
    <p class="sec-label reveal">GROWTH</p>
    <h2 class="sec-title sec-title--sm reveal">Your growth story after joining</h2>
    <p class="sec-lead reveal">There's a system to grow step by step, even from zero experience. We value potential and back your learning and challenges.</p>
    <div class="growth-flow">
      <div class="growth-step reveal"><b>STEP 01</b><h3>OJT</h3><p>Start with real work alongside seniors. We entrust small tasks first and widen the scope gradually.</p></div>
      <div class="growth-step reveal"><b>STEP 02</b><h3>Reading training</h3><p>Reading-based training to sharpen thinking. Build the ability to think for yourself and put it into words.</p></div>
      <div class="growth-step reveal"><b>STEP 03</b><h3>External training</h3><p>Choose from a rich menu of external courses such as SMBC business seminars.</p></div>
      <div class="growth-step reveal"><b>STEP 04</b><h3>Review & career</h3><p>Once a year, results against goals are reviewed and reflected in evaluation and bonus. Widen your scope of challenge.</p></div>
    </div>
  </div>
</section>

<!-- BENEFITS -->
<section class="page-section page-section--off" id="benefits">
  <div class="inner">
    <p class="sec-label reveal">BENEFITS</p>
    <h2 class="sec-title sec-title--sm reveal">Environment & benefits</h2>
    <div class="benefit-list reveal">
      <div class="benefit"><h3><b>01</b>Hours 9:00–18:00 (8h actual)</h3><p>Average overtime is about 1.2 hours a day. A focused way of working is the norm.</p></div>
      <div class="benefit"><h3><b>02</b>Holidays & leave</h3><p>125 days off a year (120 + 5 planned). 10 paid days granted after 6 months, half-day units OK. Maternity, childcare and condolence leave in place.</p></div>
      <div class="benefit"><h3><b>03</b>Training</h3><p>OJT and reading training on assignment, plus external courses (e.g. SMBC seminars). Potential over experience.</p></div>
      <div class="benefit"><h3><b>04</b>Evaluation & pay</h3><p>Once a year, results against each person's goals are reviewed, and pay and performance bonus are set individually. Effort is properly reflected.</p></div>
      <div class="benefit"><h3><b>05</b>Employee discount</h3><p>Buy our products — from bike/bicycle parts to outdoor gear and tools — at a discount. A nice perk for mobility lovers.</p></div>
      <div class="benefit"><h3><b>06</b>Selection</h3><p>About 2–4 weeks from application to offer. No restrictions by education or gender; hiring is ongoing. Three-month probation.</p></div>
    </div>
  </div>
</section>

<!-- STATEMENT BAND -->
<section class="rc-band">
  <img class="rc-band__bg" src="../../assets/img/world-ride.jpg" alt="" loading="lazy">
  <div class="rc-band__inner">
    <p class="rc-band__label">OUR FIELD</p>
    <h2 class="rc-band__title">The field to take on<br>challenges is here.</h2>
    <p class="rc-band__text">Official supplier to EXPO 2025 Osaka-Kansai. First exhibit at the Suzuka 8 Hours. A collaboration with Evangelion. New in-house brands, one after another. On a stable base, this many challenges run at once. Your idea could become the next talk of the town.</p>
  </div>
</section>

<!-- EVENTS gallery -->
<section class="page-section page-section--off" id="events">
  <div class="inner">
    <p class="sec-label reveal">EVENTS</p>
    <h2 class="sec-title sec-title--sm reveal">The kind of events we exhibit at.</h2>
    <p class="sec-lead reveal">It's not only about delivering products. We exhibit at events across Japan — including the Tokyo and Osaka Motorcycle Shows — bringing the brands we plan and our mascot “39 (Thank-you Boy)” straight to the fans. It's B2B, yet there's this much work out in the spotlight. These photos are from our booth at the Tokyo Motorcycle Show 2026.</p>
    <div class="rc-events__grid">
      <a class="rc-ev rc-ev--asmax reveal" href="../../assets/img/events/tmcs2026-asmax-booth.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/tmcs2026-asmax-booth.jpg" alt="Photo with mascot 39 and a guest at the ASMAX booth" loading="lazy">
        <span class="rc-ev__cap"><small>ASMAX BOOTH</small>A lively “name the mascot 39” quiz</span>
      </a>
      <a class="rc-ev rc-ev--suzuka reveal" href="../../assets/img/events/suzuka8h-2026.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/suzuka8h-2026.jpg" alt="Staff giving a thumbs-up on the grid at the Suzuka 8 Hours" loading="lazy">
        <span class="rc-ev__cap"><small>SUZUKA 8 HOURS</small>Our first exhibit at the Suzuka 8 Hours, before a packed grandstand</span>
      </a>
      <a class="rc-ev rc-ev--scooter reveal" href="../../assets/img/events/tmcs2026-timsun-scooter.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/tmcs2026-timsun-scooter.jpg" alt="Custom scooter display at the TIMSUN booth" loading="lazy">
        <span class="rc-ev__cap"><small>TIMSUN</small>Custom machine display</span>
      </a>
      <a class="rc-ev rc-ev--stage reveal" href="../../assets/img/events/tmcs2026-timsun-stage.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/tmcs2026-timsun-stage.jpg" alt="TIMSUN stage event" loading="lazy">
        <span class="rc-ev__cap"><small>STAGE</small>A stage telling the brand story</span>
      </a>
      <a class="rc-ev rc-ev--venue reveal" href="../../assets/img/events/tmcs2026-venue.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/tmcs2026-venue.jpg" alt="The bustling Tokyo Motorcycle Show venue" loading="lazy">
        <span class="rc-ev__cap"><small>THE VENUE</small>The buzzing Tokyo Motorcycle Show 2026</span>
      </a>
      <a class="rc-ev rc-ev--shad reveal" href="../../assets/img/events/tmcs2026-shad-cases.jpg" target="_blank" rel="noopener">
        <img src="../../assets/img/events/tmcs2026-shad-cases.jpg" alt="SHAD panniers and top cases on display" loading="lazy">
        <span class="rc-ev__cap"><small>SHAD</small>Products from the brands we handle</span>
      </a>
    </div>
  </div>
</section>

<!-- FLOW -->
<section class="page-section" id="flow">
  <div class="inner">
    <p class="sec-label reveal">SELECTION FLOW</p>
    <h2 class="sec-title sec-title--sm reveal">Selection process</h2>
    <p class="sec-lead reveal">About 2–4 weeks from application to offer. We take a careful look at your experience and potential.</p>
    <ol class="flow-steps reveal">
      <li><div><h3>Entry</h3><p>Apply from the form. Please submit your resume and work history.</p></div></li>
      <li><div><h3>Document screening</h3><p>We review your experience and direction. No restrictions by education, gender or nationality.</p></div></li>
      <li><div><h3>Interview (online OK)</h3><p>A two-way conversation about your desired role, working style and career. Office visits welcome.</p></div></li>
      <li><div><h3>Offer → Join</h3><p>A three-month probation from your start date. Get up to speed comfortably through OJT.</p></div></li>
    </ol>
    <p class="flow-note reveal">* Listed positions are hired on a rolling basis. There is no application deadline.</p>
  </div>
</section>

<!-- REQUIREMENTS -->
<section class="page-section page-section--off" id="requirements">
  <div class="inner">
    <p class="sec-label reveal">REQUIREMENTS</p>
    <h2 class="sec-title sec-title--sm reveal">Requirements</h2>
    <table class="profile-table reveal">
      <tr><th>Employment</th><td>Full-time (new-grad / mid-career)</td></tr>
      <tr><th>Hours</th><td>9:00–18:00 (8h actual). Average overtime about 1.2h/day</td></tr>
      <tr><th>Holidays</th><td>125 days/year (120 + 5 planned). Paid leave (10 days after 6 months, half-day OK), maternity, childcare and condolence leave</td></tr>
      <tr><th>Pay & review</th><td>Annual review. Results against goals reviewed; pay and performance bonus set individually</td></tr>
      <tr><th>Probation</th><td>Three months from start date (a mutual assessment period)</td></tr>
      <tr><th>Benefits</th><td>Social insurance, employee discount, training (OJT / reading / external courses)</td></tr>
      <tr><th>Location</th><td>HQ (Nipponbashi, Osaka) / Logistics Centers (Higashiosaka, Yao) — depending on role</td></tr>
      <tr><th>Eligibility</th><td>No restriction by education, gender or nationality. Potential-focused. Applicants from overseas need JLPT N1</td></tr>
    </table>
    <p class="reveal" style="margin-top:32px;display:flex;gap:14px;flex-wrap:wrap">
      <a href="#positions" class="btn-solid">View open positions</a>
      <a href="#entry" class="btn-line">Go to the entry form</a>
    </p>
  </div>
</section>

<!-- FAQ -->
<section class="page-section" id="faq">
  <div class="inner">
    <p class="sec-label reveal">FAQ</p>
    <h2 class="sec-title sec-title--sm reveal">Frequently asked questions</h2>
    <div class="rc-faq reveal">
      <details><summary>Can I thrive without experience?</summary><p>Yes. We value potential. OJT, reading training and external courses help you grow step by step.</p></details>
      <details><summary>Do I need knowledge of bikes or bicycles?</summary><p>Not particularly. Of course, if you love or are curious about mobility, you're very welcome.</p></details>
      <details><summary>Tell me about training.</summary><p>OJT on assignment and reading training to sharpen thinking, plus a rich menu of external courses such as SMBC business seminars.</p></details>
      <details><summary>How much overtime and time off?</summary><p>Overtime averages about 23 hours/month (~1.2h/day). 125 holidays a year. Paid leave granted (10 days after 6 months), half-day units possible.</p></details>
      <details><summary>How are placement and rotation decided?</summary><p>Placement is decided from your wishes at interview plus ability and aptitude. Job rotation may occur.</p></details>
      <details><summary>Is there an employee discount?</summary><p>Yes. Buy our products — bike/bicycle parts, outdoor gear, tools and more — at a discount.</p></details>
      <details><summary>How long does selection take?</summary><p>About 2–4 weeks from application to offer. Positions are hired on a rolling basis with no deadline.</p></details>
    </div>
  </div>
</section>

<!-- GLOBAL banner -->
<section class="page-section">
  <div class="inner">
    <div class="global-banner reveal">
      <div>
        <h2>Global Members Welcome</h2>
        <p>Our product development and global business teams trade overseas almost every day. Members from many countries work here, using the power of language and cultural knowledge. Your experience can shine here too. (Applying requires JLPT N1.)</p>
        <div class="global-banner__langs"><span>English</span><span>Chinese</span><span>Vietnamese</span><span>and your mother tongue</span></div>
      </div>
      <a href="global.html" class="btn-solid">For global talent</a>
    </div>
  </div>
</section>

<!-- OPEN POSITIONS -->
<section class="page-section page-section--off" id="positions">
  <div class="inner">
    <p class="sec-label reveal">OPEN POSITIONS</p>
    <h2 class="sec-title sec-title--sm reveal">Open positions</h2>
    <p class="sec-lead reveal">Click a position to see the job sheet (role, requirements, conditions). <span style="color:var(--c-red);font-weight:700">GLOBAL</span> positions trade heavily overseas.</p>
    <div class="pos-list reveal" id="posList"></div>
  </div>
</section>

<!-- ENTRY -->
<section class="page-section" id="entry">
  <div class="inner">
    <p class="sec-label reveal">ENTRY</p>
    <h2 class="sec-title sec-title--sm reveal">Entry form</h2>
    <p class="sec-lead reveal">Both mid-career and new-grad candidates can apply here. About 2–4 weeks from application to offer. No restrictions by education, gender or nationality.</p>
    <form class="entry-form reveal" id="entryForm" novalidate>
      <div class="ef-2col">
        <div class="ef-row"><label>Application type<span class="req">Required</span></label>
          <select name="type" required><option value="">Please select</option><option>Mid-career</option><option>New graduate</option><option>Long-term internship</option></select>
          <p class="ef-error">Please select</p></div>
        <div class="ef-row"><label>Desired position<span class="req">Required</span></label>
          <select name="position" id="posSelect" required><option value="">Please select</option></select>
          <p class="ef-error">Please select</p></div>
      </div>
      <div class="ef-2col">
        <div class="ef-row"><label>Name<span class="req">Required</span></label>
          <input type="text" name="name" placeholder="Taro Yamada" required>
          <p class="ef-error">Please enter your name</p></div>
        <div class="ef-row"><label>Name (phonetic)<span class="opt">Optional</span></label>
          <input type="text" name="kana" placeholder="Yamada Taro"></div>
      </div>
      <div class="ef-2col">
        <div class="ef-row"><label>Email<span class="req">Required</span></label>
          <input type="email" name="email" placeholder="you@example.com" required>
          <p class="ef-error">Please enter a valid email</p></div>
        <div class="ef-row"><label>Phone<span class="req">Required</span></label>
          <input type="tel" name="tel" placeholder="09012345678" required>
          <p class="ef-error">Please enter your phone number</p></div>
      </div>
      <div class="ef-2col">
        <div class="ef-row"><label>Area of residence<span class="opt">Optional</span></label>
          <input type="text" name="area" placeholder="Osaka"></div>
        <div class="ef-row"><label>Current status<span class="opt">Optional</span></label>
          <select name="status"><option value="">Please select</option><option>Employed</option><option>Not currently working</option><option>Student</option><option>Other</option></select></div>
      </div>
      <div class="ef-row"><label>Resume / work history<span class="opt">Optional</span></label>
        <input type="file" name="resume" accept=".pdf,.doc,.docx,.jpg,.png">
        <p class="ef-note" style="margin-top:8px">* PDF, Word or image. You can also submit later by email.</p></div>
      <div class="ef-row"><label>Motivation / self-PR<span class="opt">Optional</span></label>
        <textarea name="message" placeholder="Tell us about your experience and what you'd like to take on here."></textarea></div>
      <label class="ef-consent"><input type="checkbox" name="consent" required><span>I agree to the <a href="https://customjapan.jp/" target="_blank" rel="noopener">handling of personal information</a>. Your data is used only for the purpose of selection.<span class="req">Required</span></span></label>
      <button type="submit" class="btn-solid" style="border:none;cursor:pointer;font-family:inherit">Apply with this content</button>
      <p class="ef-note">* Applicants from overseas need JLPT N1.<br>* Contact: TEL +81-6-6563-9317 (weekdays 9:00–18:00) / MAIL recruit@customjapan.jp<br>* For the student long-term internship, see <a href="../../intern.html" style="color:var(--c-blue);text-decoration:underline">this page</a> (Japanese).</p>
    </form>
    <div class="ef-done" id="efDone">
      <h3>Thank you for applying</h3>
      <p>We'll review your details and contact you within 2–4 weeks.<br>If in a hurry, reach us at recruit@customjapan.jp.</p>
    </div>
  </div>
</section>

<!-- JOB MODAL -->
<div class="modal" id="jobModal" role="dialog" aria-modal="true" aria-hidden="true">
  <div class="modal__backdrop" data-close></div>
  <div class="modal__panel">
    <div class="modal__head">
      <button class="modal__close" data-close aria-label="Close">×</button>
      <span class="modal__div" id="mDiv"></span>
      <h3 class="modal__title" id="mTitle"></h3>
      <p class="modal__catch" id="mCatch"></p>
    </div>
    <div class="modal__body">
      <p class="modal__work" id="mWork"></p>
      <p class="modal__sub">Who we welcome</p>
      <ul class="modal__list" id="mWant"></ul>
      <p class="modal__sub">Welcome experience / skills</p>
      <ul class="modal__list" id="mWelcome"></ul>
      <p class="modal__sub">Conditions</p>
      <table class="modal__table">
        <tr><th>Employment</th><td id="mEmploy"></td></tr>
        <tr><th>Location</th><td id="mPlace"></td></tr>
        <tr><th>Hours</th><td id="mHours"></td></tr>
        <tr><th>Pay</th><td id="mSalary"></td></tr>
        <tr><th>Holidays</th><td id="mHoliday"></td></tr>
        <tr><th>Benefits</th><td id="mBenefit"></td></tr>
        <tr><th>Selection</th><td id="mFlow"></td></tr>
      </table>
      <div class="modal__apply"><a href="#entry" class="btn-solid" data-close id="mApply">Apply for this position</a></div>
    </div>
  </div>
</div>

<!-- INTERVIEW MODAL -->
<div class="modal" id="ivModal" role="dialog" aria-modal="true" aria-hidden="true">
  <div class="modal__backdrop" data-close></div>
  <div class="modal__panel">
    <div class="modal__head">
      <button class="modal__close" data-close aria-label="Close">×</button>
      <span class="modal__div" id="ivNo"></span>
      <h3 class="modal__title" id="ivTitle"></h3>
      <p class="modal__catch" id="ivMeta"></p>
    </div>
    <div class="modal__body">
      <div class="iv-modal__head">
        <img id="ivImg" src="" alt="" loading="lazy">
        <div><p class="modal__sub" style="margin-top:0">Division</p><p id="ivDept" style="font-size:13px;font-weight:700"></p><p id="ivRole" style="font-size:12px;color:var(--c-gray);margin-top:4px"></p></div>
      </div>
      <div id="ivBody"></div>
      <div class="modal__apply"><a href="#entry" class="btn-solid" data-close>I want to work here — apply</a></div>
    </div>
  </div>
</div>

<footer class="footer">
  <div class="inner">
    <div class="footer__top">
      <div class="footer__company">
        <img src="../../assets/logo/cj-logo-white-text.svg" alt="CUSTOM JAPAN" class="footer__logo">
        <p class="footer__address">Custom Japan Co., Ltd.<br>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>Careers: recruit@customjapan.jp</p>
      </div>
      <nav class="footer__nav">
        <a href="#data">DATA</a><a href="#jobs">JOBS</a><a href="#people">PEOPLE</a><a href="#benefits">BENEFITS</a>
        <a href="global.html">GLOBAL</a><a href="../index.html">日本語</a><a href="../../en/index.html">Corporate</a>
      </nav>
      <div class="footer__contact"><p>Apply here</p><a href="#entry" class="btn-line btn-line--light">Entry form</a></div>
    </div>
    <p class="footer__copy">&copy; Custom Japan Co., Ltd. All Rights Reserved.</p>
  </div>
</footer>
</main>'''

# ---- English inline script (paths ../../assets, English UI strings) ----
INDEX_SCRIPT = '''
<script src="../../js/vendor/gsap.min.js"></script>
<script src="../../js/vendor/ScrollTrigger.min.js"></script>
<script src="../../js/vendor/lenis.min.js"></script>
<script src="../../js/main.js"></script>
<script src="jobs-data.js"></script>
<script src="interviews-data.js"></script>
<script>
(function(){
  var jobs = window.CJ_JOBS || [], common = window.CJ_JOB_COMMON || {};
  var esc = function(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); };
  var list = document.getElementById('posList'), sel = document.getElementById('posSelect');
  if (list) jobs.forEach(function(j){
    var btn=document.createElement('button'); btn.type='button'; btn.className='pos-row'; btn.setAttribute('data-job',j.id);
    btn.innerHTML='<span class="pos-row__div'+(j.global?' is-global':'')+'">'+(j.global?'GLOBAL':esc(j.div))+'</span>'+
      '<span class="pos-row__title">'+esc(j.title)+'</span><span class="pos-row__cta"><span>View details</span></span>';
    btn.addEventListener('click',function(){openJob(j.id);}); list.appendChild(btn);
  });
  if (sel){ jobs.forEach(function(j){ var o=document.createElement('option'); o.value=j.title; o.textContent=j.title; sel.appendChild(o); });
    var o2=document.createElement('option'); o2.value='Other / Undecided'; o2.textContent='Other / Undecided'; sel.appendChild(o2); }
  var modal=document.getElementById('jobModal');
  var set=function(id,v){var e=document.getElementById(id); if(e) e.textContent=v;};
  var fillList=function(id,arr){var e=document.getElementById(id); if(!e)return; e.innerHTML=''; (arr||[]).forEach(function(t){var li=document.createElement('li'); li.textContent=t; e.appendChild(li);});};
  function openJob(id){var j=jobs.filter(function(x){return x.id===id;})[0]; if(!j)return;
    var d=document.getElementById('mDiv'); d.textContent=j.global?'GLOBAL / '+j.div:j.div; d.className='modal__div'+(j.global?' is-global':'');
    set('mTitle',j.title); set('mCatch',j.catch); set('mWork',j.work); fillList('mWant',j.want); fillList('mWelcome',j.welcome);
    set('mEmploy',common.employ); set('mPlace',common.place); set('mHours',common.hours); set('mSalary',common.salary);
    set('mHoliday',common.holiday); set('mBenefit',common.benefit); set('mFlow',common.flow);
    document.getElementById('mApply').onclick=function(){closeModal(); if(sel) sel.value=j.title; if(window.lenis) window.lenis.scrollTo('#entry',{offset:-70,duration:1.2});};
    modal.classList.add('is-open'); modal.setAttribute('aria-hidden','false'); document.documentElement.style.overflow='hidden';}
  function closeModal(){modal.classList.remove('is-open'); modal.setAttribute('aria-hidden','true'); document.documentElement.style.overflow='';}
  if(modal) modal.querySelectorAll('[data-close]').forEach(function(el){el.addEventListener('click',function(e){if(el.id!=='mApply'){e.preventDefault();} closeModal();});});
  var ivs=window.CJ_INTERVIEWS||[], pGrid=document.getElementById('peopleGrid');
  if(pGrid) ivs.forEach(function(v){
    var b=document.createElement('button'); b.type='button'; b.className='person'; b.setAttribute('data-iv',v.id);
    b.innerHTML='<div class="person__img"><img src="../../assets/img/'+esc(v.img)+'" alt="" loading="lazy"></div>'+
      '<div class="person__body"><p class="person__meta">INTERVIEW '+esc(v.no)+' — '+esc(v.dept)+'</p>'+
      '<h3>'+esc(v.title)+'</h3><p>'+esc(v.meta)+'</p><span class="person__more">Read interview</span></div>';
    b.addEventListener('click',function(){openIv(v.id);}); pGrid.appendChild(b);
  });
  var ivModal=document.getElementById('ivModal');
  function openIv(id){var v=ivs.filter(function(x){return x.id===id;})[0]; if(!v||!ivModal)return;
    set('ivNo','INTERVIEW '+v.no); set('ivTitle',v.title); set('ivMeta',v.meta); set('ivDept',v.dept); set('ivRole',v.role);
    var img=document.getElementById('ivImg'); if(img) img.src='../../assets/img/'+v.img;
    var body=document.getElementById('ivBody'); if(body){body.innerHTML=''; (v.body||[]).forEach(function(t){var p=document.createElement('p'); p.textContent=t; body.appendChild(p);});}
    ivModal.querySelector('.modal__panel').scrollTop=0; ivModal.classList.add('is-open'); ivModal.setAttribute('aria-hidden','false'); document.documentElement.style.overflow='hidden';}
  function closeIv(){if(!ivModal)return; ivModal.classList.remove('is-open'); ivModal.setAttribute('aria-hidden','true'); document.documentElement.style.overflow='';}
  if(ivModal) ivModal.querySelectorAll('[data-close]').forEach(function(el){el.addEventListener('click',function(e){if(!el.classList.contains('btn-solid')){e.preventDefault();} closeIv();});});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeModal(); closeIv();}});
  var form=document.getElementById('entryForm'), done=document.getElementById('efDone');
  if(form){form.addEventListener('submit',function(e){e.preventDefault(); var ok=true;
    form.querySelectorAll('[required]').forEach(function(f){var row=f.closest('.ef-row')||f.closest('.ef-consent');
      var bad=(f.type==='checkbox')?!f.checked:!String(f.value).trim()||(f.type==='email'&&!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(f.value));
      if(row&&row.classList) row.classList.toggle('is-invalid',bad); if(bad) ok=false;});
    if(!ok){var first=form.querySelector('.is-invalid'); if(first&&window.lenis) window.lenis.scrollTo(first,{offset:-120,duration:.8}); return;}
    form.classList.add('is-submitted'); if(done){done.style.display='block'; if(window.lenis) window.lenis.scrollTo(done,{offset:-120,duration:.8});}});
   form.querySelectorAll('input,select,textarea').forEach(function(f){f.addEventListener('input',function(){var r=f.closest('.ef-row')||f.closest('.ef-consent'); if(r&&r.classList) r.classList.remove('is-invalid');});});}
})();
</script>
</body>
</html>'''

(OUT / "index.html").write_text(INDEX_HEAD + INDEX_BODY + INDEX_SCRIPT, encoding="utf-8")
print("wrote", OUT / "index.html")

# ================= EN DATA FILES =================
(OUT / "jobs-data.js").write_text('''/* Job data (EN) — generated by build-recruit-en.py */
window.CJ_JOBS = [
  {id:"mobility",div:"Product Development",global:false,title:"Next-gen Mobility — Development, Planning & QC",
   catch:"Creating the mobility of the future.",
   work:"Beyond the frame of cars and bikes, we shape \\"mobility that doesn't yet exist\\" by reading domestic and overseas trends. You'll plan, develop and manage quality for our electric mobility brand eXs, cutting into niche needs that big markets overlook.",
   want:["Interested in creating a product from zero","Can research market trends and form hypotheses","Can take responsibility for quality and safety"],
   welcome:["Experience in a maker, product planning or QC","Languages (English, Chinese, etc.)"]},
  {id:"global-biz",div:"Global Business",global:true,title:"Global Business (Overseas Sales & Development)",
   catch:"Shaping new business across Asian markets.",
   work:"Targeting ASEAN (Vietnam, Cambodia, Philippines, Indonesia), China and Taiwan, you'll build relationships with overseas makers, distributors and dealers. Beyond dealer sales and channel development, you'll take on cross-border EC and digital marketing, covering market research, product planning, brand rollout and sales strategy.",
   want:["Want to take on building business overseas","Can think and act in markets without a set answer","Want to use business-level language skills"],
   welcome:["Overseas sales / trade / business development","English, Chinese, etc.","Overseas applicants: JLPT N1 required"]},
  {id:"global-buyer",div:"Product Development",global:true,title:"Overseas Buyer (Development, Buying & QC)",
   catch:"Finding products worldwide, creating hits.",
   work:"You'll search worldwide for parts, accessories, tools and chemicals for bikes, bicycles and cars, and handle everything from productization to buying and sales. Discover \\"unknown, attractive products\\" and deliver them to customers in Japan. On-site negotiation abroad is part of the job.",
   want:["Want to sharpen an eye for products that sell","Can negotiate while enjoying different cultures","Have the imagination to shape latent needs"],
   welcome:["Buyer / purchasing / trade experience","Language skills (English, Chinese, etc.)","Overseas applicants: JLPT N1 required"]},
  {id:"marketing",div:"Marketing",global:false,title:"BtoB/BtoC Marketing & Promotion Planner",
   catch:"Driving EC growth through marketing.",
   work:"You'll run our own EC sites and marketplaces for BtoB/BtoC, plus marketing via print catalogs and DM. We've built a BI analytics base from core-system data, and next aim for scenario marketing with MA tools — optimizing customer experience from data.",
   want:["Can design and verify measures from data","Interested in both BtoB and BtoC marketing","Want to introduce new methods yourself"],
   welcome:["EC operation / ad ops / data analysis","Experience with BI/MA tools"]},
  {id:"engineer",div:"ICT & Engineering",global:false,title:"Frontend / Cloud Engineer",
   catch:"Toward the world's No.1 specialist EC.",
   work:"The motorcycle industry is called the most legacy of vehicle industries — and we take on cutting-edge development there. Our flagship is a \\"bike fitment search\\" built on one of the world's largest fitment databases, delivered as a self-built headless EC system. Expansion into cars is underway.",
   want:["Want to take on the cutting edge in a legacy field","Want to design your own product proactively","Drawn to working with large-scale data"],
   welcome:["Frontend / cloud development experience","Headless CMS / EC build experience"]},
  {id:"ict",div:"ICT & Engineering",global:false,title:"Internal SE / Information Systems",
   catch:"Supporting internal ICT, creating the future.",
   work:"The unsung hero supporting internal systems and networks. With a view to \\"how a new system helps customers\\" and \\"how much process improvement raises internal efficiency,\\" you'll meet with each division to build and improve systems.",
   want:["Enjoy designing and shaping new mechanisms","Can solve problems through dialogue with divisions"],
   welcome:["Internal SE / information systems / infrastructure"]},
  {id:"ec-ops",div:"Marketing",global:false,title:"EC Order Operator",
   catch:"The pivotal operation that delivers to customers.",
   work:"You reliably process customer orders and deliver products smoothly. Beyond order entry, shipping arrangement and inquiry handling, you'll also manage part-time staff — a role that supports the whole organization.",
   want:["Good at accurate, speedy admin work","Want to take on a role leading a team"],
   welcome:["Order handling / customer support / EC operation"]},
  {id:"domestic-buyer",div:"Product Development",global:false,title:"Domestic Buyer (Buying, Negotiation & Planning)",
   catch:"Buyer work from purchasing to promotion.",
   work:"You'll develop new suppliers, negotiate with existing ones, and plan sales and promotions. Main products are bike, bicycle and car parts, tools, chemicals and outdoor goods. Spot products that sell, and take them through promotion and branding.",
   want:["Enjoy finding and conveying a product's appeal","Find reward in negotiation and numbers"],
   welcome:["Buyer / purchasing / sales-planning experience"]},
  {id:"logistics",div:"SCM & Fulfillment",global:false,title:"Logistics Operator",
   catch:"The logistics heart behind same-day shipping.",
   work:"You'll manage the whole logistics center so products reach customers smoothly and accurately. From inbound/outbound, inventory, quality and staff management to cost control, you support the foundation that keeps professional procurement moving.",
   want:["Want to turn on-site insight into systems","Interested in team management"],
   welcome:["Logistics / warehouse management / SCM"]},
  {id:"corporate",div:"Corporate",global:false,title:"Accounting / General Affairs / HR",
   catch:"Building the base of a growing company.",
   work:"As accounting, general affairs and HR, you support the whole company from the ground up. In an expansion phase (20 years, 107 employees), there's the fun of building the systems themselves, not just running existing operations.",
   want:["Want to support company growth from the base","Interested in building systems and structures"],
   welcome:["Experience in accounting, GA or HR"]}
];
window.CJ_JOB_COMMON = {
  employ:"Full-time (mid-career / new-grad). 3-month probation.",
  place:"HQ (Nipponbashi, Osaka). Logistics Operator: Logistics Centers (Higashiosaka / Yao).",
  hours:"9:00–18:00 (8h actual). Average overtime ~1.2h/day.",
  salary:"Offered at interview based on experience and ability (reviewed annually).",
  holiday:"125 days/year (120 + 5 planned). Maternity, childcare and condolence leave.",
  benefit:"Social insurance, employee discount, training (OJT / reading / external).",
  flow:"Entry → Document screening → Interview (online OK) → Offer (about 2–4 weeks)."
};
''', encoding="utf-8")
print("wrote", OUT / "jobs-data.js")

(OUT / "interviews-data.js").write_text('''/* Interview data (EN) — generated by build-recruit-en.py */
window.CJ_INTERVIEWS = [
  {id:"iv1",img:"iv-01.jpg",no:"01",dept:"SCM & Fulfillment",meta:"Joined 2019 / K.I.",role:"Logistics Center #1, Center Manager",
   title:"Turning the floor's voice into systems, supporting the logistics heart with sharp foresight",
   body:["I joined as a part-timer, drawn to \\"work that supports the flow of people and goods.\\" After about three years on the floor, a turning point came when a staff member said \\"we want you to do it\\" and I was entrusted to lead the floor.",
    "Now, as manager of Logistics Center #1, I handle inbound/outbound progress, staffing, efficiency and safety. What I value most is \\"reading ahead\\": based on a week of shipping forecasts, I adjust shifts in advance on high-volume days so the floor never stops."]},
  {id:"iv2",img:"iv-02.jpg",no:"02",dept:"Product Development",meta:"Joined 2014 / Y.N.",role:"Domestic buying / procurement",
   title:"\\"Search until you find it\\" — gritty buying and team bonds that support the company's evolution",
   body:["I joined as a part-timer in the company's founding days. Back then there were many fax and phone orders and no logistics system; I did picking and packing. I've watched the company grow from the floor ever since.",
    "Now in product development, I handle domestic buying, price negotiation and new-supplier development. What I value most is to \\"search until I find it\\" even when things go off-script. The charm here is the stimulation from members of diverse backgrounds — a colleague taught me everything from Excel functions to clear document design."]},
  {id:"iv3",img:"iv-03.jpg",no:"03",dept:"SCM & Fulfillment",meta:"Joined 2021 / N.T.",role:"Operations / Customer Center",
   title:"What supported my leap from zero experience: teammates and a focus on how I convey things",
   body:["I'd always worked in food service, but wanted to try a new field, so I looked for desk work. The deciding factor was a 10-minute bike commute from home — a stress-free environment mattered a lot to me.",
    "Now I mainly handle email and phone inquiries. Precisely because it isn't face-to-face, tone of voice and word choice — \\"how you convey\\" — matter most. Even when caught between makers and customers, I make sure to hear the customer out fully. Even without experience, I keep taking on challenges with my teammates' support."]},
  {id:"iv4",img:"iv-04.jpg",no:"04",dept:"Product Development (Next-gen Mobility)",meta:"Joined 2019 / M.K.",role:"Team Leader",
   title:"Opening up next-gen mobility, contributing to the company's growth",
   body:["Studying Chinese as a student and doing buying on business trips to China in a previous job drew me to trade and procurement. At the interview, many people — including the CEO — had great character, and I felt I could take on challenges here with peace of mind.",
    "This job can't do without dealing with overseas makers. When quality issues arise, negotiations can stall over responsibility, and Japanese common sense doesn't always apply. Even so, I stay calm and persistent. There's the thrill of carving out a new field — next-gen mobility — with my own hands."]},
  {id:"iv5",img:"iv-07.jpg",no:"05",dept:"ICT & Engineering",meta:"Joined 2023 / T.S.",role:"Internal SE / systems maintenance",
   title:"At a growing company, taking on the making of new mechanisms",
   body:["After information management I was moved to general affairs at my previous job, but my wish to keep working with systems was strong, so I changed jobs. I wanted an environment where I could secure my own time and continue long-term.",
    "Now I mainly maintain the newly introduced sales-management system. Beyond investigating issues, I turn improvement requests from divisions into reality. The reward is helping other divisions work more efficiently — I like hearing what troubles them and thinking together about how to make things easier."]},
  {id:"iv6",img:"iv-06.jpg",no:"06",dept:"Marketing (B2C)",meta:"Joined 2019 / A.H.",role:"Leader / EC marketplace ops",
   title:"From part-timer to full-time — growth found through a new challenge",
   body:["In my previous BtoC customer-facing job I found reward, but wanted a calmer environment to show my strengths. I applied to our BtoB phone-support opening and started with two years of operations as a part-timer.",
    "Now in marketing, I handle product-info improvement and promotion planning on Amazon, Rakuten and Yahoo!. I started with zero experience, but my manager remembered I'd said \\"I like design and illustration,\\" which led to the move. The perspective I built in operations now helps my work."]},
  {id:"iv7",img:"iv-05.jpg",no:"07",dept:"Product Development",meta:"Joined 2024 / S.Y.",role:"Overseas supplier procurement",
   title:"Raising procurement precision, creating new value for the organization",
   body:["During job hunting, an event introduced by my university professor was my first meeting with the company. The in-house electric kickboard I saw there drew me in — \\"I want to work at a company like this.\\"",
    "First I spent a year and a half in logistics, handling inbound/outbound and inventory. Then, at my own request, I moved to product development and now handle procurement from overseas suppliers. Being entrusted with sales-linked work as a new grad is a big reward; the sense of achievement when I prevent shortages and hit the sales plan is exceptional. Monthly training builds expertise too."]}
];
''', encoding="utf-8")
print("wrote", OUT / "interviews-data.js")

# ================= GLOBAL page (EN) =================
GLOBAL_CSS = re.search(r"<style>.*?</style>", (ROOT/"recruit"/"global.html").read_text(encoding="utf-8"), re.S).group(0)
GLOBAL = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For Global Talent | Custom Japan Co., Ltd. RECRUIT</title>
<meta name="description" content="At Custom Japan, staff from overseas thrive at the front line of product development and global business. Bring your language and experience to Japan's mobility business. (Applying requires JLPT N1.)">
<link rel="icon" href="../../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/style.css">
{GLOBAL_CSS}
{seo("global.html","For Global Talent | Custom Japan Co., Ltd.","Bring your language and experience to Japan's mobility business.","global.html")}
</head>
<body>
<header class="header header--solid" id="header">
  <a href="index.html" class="header__logo">
    <img src="../../assets/logo/cj-logo-white-text.svg" alt="" class="header__logo-white" aria-hidden="true">
    <img src="../../assets/logo/cj-logo-black-text.svg" alt="Custom Japan Co., Ltd." class="header__logo-color">
  </a>
  <nav class="header__nav">
    <a href="index.html">RECRUIT TOP</a><a href="index.html#jobs">JOBS</a><a href="index.html#people">PEOPLE</a><a href="index.html#benefits">BENEFITS</a>
    <a href="../global.html" class="header__lang">日本語</a>
    <a href="index.html#entry" class="header__recruit"><span class="header__recruit-en">ENTRY</span><span class="header__recruit-jp">Apply</span></a>
  </nav>
  <button class="header__menu-btn" id="menuBtn" aria-controls="mobileMenu" aria-expanded="false" aria-label="Menu"><span></span><span></span></button>
</header>
<div class="mobile-menu" id="mobileMenu"><nav>
  <a href="index.html">RECRUIT TOP</a><a href="index.html#jobs">JOBS</a><a href="index.html#people">PEOPLE</a><a href="index.html#benefits">BENEFITS</a>
  <a href="../global.html">日本語</a><a href="index.html#entry" class="mobile-menu__recruit">ENTRY — Apply</a>
</nav></div>
<button class="mascot-top" id="mascotTop" aria-label="Back to top"><img src="../../assets/logo/cj-mascot.svg" alt=""><span>TOP</span></button>
<main>
<section class="gl-hero">
  <div class="inner">
    <p class="gl-hero__label">FOR GLOBAL TALENT</p>
    <h1 class="gl-hero__title">Bring your language and experience<br>to Japan's mobility business.</h1>
    <p class="gl-hero__lead">Members from many countries work at Custom Japan.<br class="pc">Our product development and global business teams trade overseas every day. We need your strength.</p>
    <span class="gl-note">Applying requires JLPT N1 (business-level Japanese).</span>
  </div>
</section>
<div class="crumb"><a href="../../en/index.html">Corporate</a><span>/</span><a href="index.html">Careers</a><span>/</span>For Global Talent</div>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">INTERVIEW MOVIE</p>
    <h2 class="sec-title sec-title--sm reveal">A message from our team</h2>
    <p class="sec-lead reveal">Hear from colleagues who work here every day. See who they are and how it feels to work at Custom Japan.</p>
    <div class="gl-video reveal">
      <video src="../../assets/video/interview-global.mp4" poster="../../assets/img/iv-global-poster.jpg" controls playsinline preload="none"></video>
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">WHY GLOBAL TALENT</p>
    <h2 class="sec-title sec-title--sm reveal">Three reasons your strength shines</h2>
    <div class="gl-points">
      <div class="gl-point reveal"><b>REASON 01</b><h3>Overseas trade, every day</h3><p>We source products from makers worldwide — China, Taiwan, Vietnam, Cambodia, the Philippines, Indonesia, Europe. Knowing a partner country's language and culture is itself a major strength.</p></div>
      <div class="gl-point reveal"><b>REASON 02</b><h3>Mother tongue + Japanese widens your career</h3><p>Overseas buyers negotiate with local makers; the global business team opens ASEAN markets. Work that "Japanese-only" or "mother-tongue-only" can't do exists here. You work as a business owner, not an interpreter.</p></div>
      <div class="gl-point reveal"><b>REASON 03</b><h3>Already a multinational team</h3><p>Staff from overseas are active at the front line of product development and global trade. This isn't a workplace with "just one foreigner." A place where those who can both debate in Japanese and connect to the world in their mother tongue can shine.</p></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">POSITIONS</p>
    <h2 class="sec-title sec-title--sm reveal">Especially welcome positions</h2>
    <div class="gl-points">
      <div class="gl-point reveal"><b>GLOBAL BUYER</b><h3>Overseas Buyer (Development, Buying)</h3><p>Find products around the world and sell them in Japan. Negotiate with overseas makers, check quality and plan products. You may travel to overseas shows and factories.</p></div>
      <div class="gl-point reveal"><b>GLOBAL BUSINESS</b><h3>Global Business (Sales & Development)</h3><p>Build new business in Vietnam, Cambodia, the Philippines, Indonesia, China and Taiwan. Find distributors, build cross-border EC and more.</p></div>
      <div class="gl-point reveal"><b>AND MORE</b><h3>All positions are open</h3><p>You can apply to any role — marketing, engineering, EC operations and more. No restriction by nationality. <a href="index.html#jobs" style="color:var(--c-blue);text-decoration:underline">See our work</a>.</p></div>
    </div>
  </div>
</section>

<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">Q&amp;A</p>
    <h2 class="sec-title sec-title--sm reveal">Frequently asked questions</h2>
    <div class="faq reveal" style="max-width:860px">
      <details style="border-bottom:1px solid var(--c-line);padding:6px 4px"><summary style="cursor:pointer;font-weight:700;font-size:14.5px;padding:18px 0;list-style:none">How much Japanese do I need?</summary><p style="font-size:13px;color:#3c4149;padding:0 0 20px 0;line-height:2">JLPT N1 is required to apply. Internal communication and negotiations are mainly in Japanese, so we ask for business-level Japanese. On that basis, your mother tongue and overseas experience become strengths.</p></details>
      <details style="border-bottom:1px solid var(--c-line);padding:6px 4px"><summary style="cursor:pointer;font-weight:700;font-size:14.5px;padding:18px 0;list-style:none">Can I ask about visa status?</summary><p style="font-size:13px;color:#3c4149;padding:0 0 20px 0;line-height:2">Yes. Tell us your current status and desired position, and let's discuss it at the interview. You can also ask by email (recruit@customjapan.jp).</p></details>
      <details style="border-bottom:1px solid var(--c-line);padding:6px 4px"><summary style="cursor:pointer;font-weight:700;font-size:14.5px;padding:18px 0;list-style:none">How does selection work?</summary><p style="font-size:13px;color:#3c4149;padding:0 0 20px 0;line-height:2">About 2–4 weeks from application to offer. No restriction by education, gender or nationality. We ask for a resume in Japanese; if unsure, feel free to consult us.</p></details>
      <details style="border-bottom:1px solid var(--c-line);padding:6px 4px"><summary style="cursor:pointer;font-weight:700;font-size:14.5px;padding:18px 0;list-style:none">Do I need to know cars or bikes?</summary><p style="font-size:13px;color:#3c4149;padding:0 0 20px 0;line-height:2">No. You'll learn naturally on the job. If you love vehicles or gadgets, all the better.</p></details>
    </div>
  </div>
</section>

<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">HOW TO APPLY</p>
    <h2 class="sec-title sec-title--sm reveal">How to apply</h2>
    <ol class="gl-steps reveal">
      <li><span>Apply from the entry form<small>Choose a position you're interested in on the Careers top.</small></span></li>
      <li><span>Interview (online OK)<small>You can casually discuss Japanese level and visa status here.</small></span></li>
      <li><span>Selection (about 2–4 weeks)<small>We look at your experience and potential.</small></span></li>
      <li><span>Offer → Join<small>Three-month probation. Get up to speed comfortably through OJT.</small></span></li>
    </ol>
    <div class="reveal" style="margin-top:44px;display:flex;gap:16px;flex-wrap:wrap">
      <a href="index.html#entry" class="btn-solid">Apply</a>
      <a href="mailto:recruit@customjapan.jp" class="btn-line">Ask by email</a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="inner">
    <div class="footer__top">
      <div class="footer__company">
        <img src="../../assets/logo/cj-logo-white-text.svg" alt="CUSTOM JAPAN" class="footer__logo">
        <p class="footer__address">Custom Japan Co., Ltd.<br>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>Careers: recruit@customjapan.jp</p>
      </div>
      <nav class="footer__nav"><a href="index.html">RECRUIT TOP</a><a href="index.html#jobs">JOBS</a><a href="index.html#people">PEOPLE</a><a href="../global.html">日本語</a><a href="../../en/index.html">Corporate</a></nav>
      <div class="footer__contact"><p>Apply here</p><a href="index.html#entry" class="btn-line btn-line--light">Entry form</a></div>
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
</html>'''
(OUT / "global.html").write_text(GLOBAL, encoding="utf-8")
print("wrote", OUT / "global.html")

# ================= DIVISIONS (EN) =================
DIV_CSS = re.search(r"<style>.*?</style>", (ROOT/"recruit"/"division"/"product.html").read_text(encoding="utf-8"), re.S).group(0)
DIVS = [
 {"slug":"product","code":"R&D / BUYING","jp":"Product Development","en":"PRODUCT DEVELOPMENT","img":"../../../assets/img/recruit-division-product-hero.jpg","global":True,
  "lead":"Find products worldwide, create hits in Japan. Build next-gen mobility from zero.",
  "body":"The heart of Custom Japan, which goes beyond a parts wholesaler to own “planning through sales.” We search worldwide for parts, accessories, tools and chemicals for bikes, bicycles and cars, handling productization, buying and sales end to end. We also take on “mobility that doesn't yet exist.” Trade with overseas is heavy, and a multinational team is active.",
  "mission":[("See what sells","The imagination to shape “needs customers haven't noticed.” The joy when a product you sourced becomes a hit is unique to this work."),("Negotiate with the world","Visit sites abroad and negotiate directly with makers and distributors. Stand at the front line of global business while enjoying different cultures."),("Create future mobility","As needs diversify, chances lie in niche problems — and cutting into them is our strength.")],
  "positions":[("Next-gen Mobility — Development, Planning & QC","Shape next-gen mobility (incl. eXs) by reading domestic and overseas trends."),("Overseas Buyer (Development, Buying & QC)","Discover “unknown” products worldwide and deliver them to customers in Japan."),("Domestic Buyer (Buying, Negotiation & Planning)","From new-supplier development to promotion and branding — a role of many decisions.")]},
 {"slug":"global","code":"GLOBAL","jp":"Global Business","en":"GLOBAL BUSINESS","img":"../../../assets/img/recruit-division-global-hero.jpg","global":True,
  "lead":"Across Asian markets, shape business without a set answer — with your own hands.",
  "body":"A division creating new business opportunities in overseas markets centered on ASEAN, driving group growth. Targeting Vietnam, Cambodia, the Philippines, Indonesia, China and Taiwan, you build relationships with overseas makers, distributors and dealers. Beyond dealer sales and channel development, you take on cross-border EC and digital marketing — covering research, planning, brand rollout and strategy.",
  "mission":[("Decide in markets without answers","A role where you think, act and shape business yourself. Big growth for those who want to build business overseas."),("Build new channels","Beyond dealer sales, launch the channels of the future — cross-border EC and digital marketing."),("Move the company horizontally","Work with marketing, logistics and product development to drive global business end to end.")],
  "positions":[("Global Business (Overseas Sales & Development)","Dealer development, cross-border EC, research to strategy across ASEAN, China and Taiwan.")]},
 {"slug":"marketing","code":"MARKETING","jp":"Marketing","en":"MARKETING","img":"../../../assets/img/recruit-division-marketing-hero.jpg","global":False,
  "lead":"130k members and 500k SKUs. Drive EC growth, starting from data.",
  "body":"We run our own EC sites and marketplaces for BtoB/BtoC, plus marketing via print catalogs and DM. We've built a BI analytics base from core-system data, and next aim for scenario marketing with MA tools — optimizing customer experience from data.",
  "mission":[("Decide with data","Rather than instinct alone, build measures on BI-visualized data and verify results."),("Move both BtoB and BtoC","The breadth of working on both wholesale for pro shops and EC for end users."),("Introduce new methods","A phase to launch new mechanisms yourself, such as MA-driven scenario marketing.")],
  "positions":[("BtoB/BtoC Marketing & Promotion Planner","Run EC / marketplaces / print & DM, and design data-driven measures."),("EC Order Operator","Order handling, shipping, inquiries — plus staff management.")]},
 {"slug":"ict","code":"ENGINEERING","jp":"ICT & Engineering","en":"ICT & ENGINEERING","img":"../../../assets/img/recruit-division-ict-hero.jpg","global":False,
  "lead":"In “the most legacy vehicle industry,” build the world's No.1 EC service.",
  "body":"The motorcycle industry is called the most legacy of vehicle industries — and we take on cutting-edge development there. Our flagship is a “bike fitment search” built on one of the world's largest fitment databases, delivered as a self-built headless EC. We're advancing toward the No.1 specialist EC.",
  "mission":[("Move world-class data","Half a century of parts and fitment data — a unique asset whose value rises in the AI era and rivals can't copy."),("Design it yourself","Headless EC built in-house. Take on the mission to “build the world's No.1 EC connecting every part and vehicle.”"),("Support all divisions with ICT","Through process improvement and system building, raise internal productivity.")],
  "positions":[("Frontend / Cloud Engineer","Build one of the world's largest bike-fitment DBs and a headless EC in-house."),("Internal SE / Information Systems","Build and improve internal systems and networks to support every division.")]},
 {"slug":"scm","code":"LOGISTICS","jp":"SCM & Fulfillment","en":"SCM & FULFILLMENT","img":"../../../assets/img/recruit-division-scm-hero.jpg","global":False,
  "lead":"The logistics heart behind same-day shipping. Turn the floor's voice into systems.",
  "body":"With domestic and overseas hubs and our own systems, we control the whole supply chain and achieve same-day shipping of in-stock items. Delivering 850k products reliably and smoothly — the backbone that keeps professional procurement moving. Improvements noticed on the floor become company-wide systems.",
  "mission":[("Turn the floor into systems","Daily insight and “reading ahead” feed directly into workflow and system improvement. A culture that welcomes proposals."),("Sharpen the physical-world edge","A logistics network that AI can't replace. Support the source of competitiveness — 500k SKUs, same-day shipping."),("Support as a team","Gain the perspective to move the whole organization, including part-time staff management.")],
  "positions":[("Logistics Operator","On-site work at the logistics center supporting same-day shipping. Proposals become systems.")]},
 {"slug":"corporate","code":"CORPORATE","jp":"Corporate","en":"CORPORATE","img":"../../../assets/img/recruit-division-corporate-hero.jpg","global":False,
  "lead":"Build the base of a growing company. A phase where you shape the systems.",
  "body":"As accounting, general affairs and HR, you support the company's growth from the ground up. In an expansion phase (20 years, 107 employees), there's the fun of building systems themselves, not just running existing operations. A role that supports a challenging front line with a secure environment.",
  "mission":[("Build the systems","In an expanding company, create a workable environment (125 days off, DX, etc.) with your own hands."),("Connect all divisions","Accounting, GA and HR are where company-wide information gathers. Cultivate a whole-company view."),("Support challenge","Support an aggressive business with solid defense — a pivotal role balancing security and challenge.")],
  "positions":[("Accounting / General Affairs / HR","Corporate work supporting company growth, from building systems up.")]}
]
DNAV = [("../index.html","RECRUIT TOP"),("../index.html#jobs","JOBS"),("../index.html#people","PEOPLE"),("../index.html#benefits","BENEFITS")]
def div_page(d, others):
    nav = "\n".join(f'    <a href="{h}">{t}</a>' for h,t in DNAV)
    tag = '<span class="dv-tag dv-tag--global">GLOBAL — a division trading heavily overseas</span>' if d["global"] else ""
    mission = "\n".join(f'      <div class="dv-mission reveal"><h3>{m[0]}</h3><p>{m[1]}</p></div>' for m in d["mission"])
    positions = "\n".join(f'      <div class="dv-pos reveal"><h3>{p[0]}</h3><p>{p[1]}</p></div>' for p in d["positions"])
    others_html = "\n".join(f'      <a class="dv-other reveal" href="{o["slug"]}.html"><b>{o["en"]}</b><span>{o["jp"]}</span></a>' for o in others)
    gtag = '<p class="reveal" style="margin-top:22px;font-size:12.5px"><a href="../global.html" style="color:var(--c-blue);text-decoration:underline">For global talent — you can thrive in this division (JLPT N1 required to apply)</a></p>' if d["global"] else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['jp']} | Careers Custom Japan Co., Ltd.</title>
<meta name="description" content="Custom Japan {d['jp']} — {d['lead']}">
<link rel="icon" href="../../../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../../css/style.css">
{DIV_CSS.replace("../../assets","../../../assets")}
<link rel="canonical" href="{BASE}/recruit/en/division/{d['slug']}.html">
<meta property="og:type" content="website"><meta property="og:title" content="{d['jp']} | Careers Custom Japan">
<meta property="og:locale" content="en_US"><meta property="og:image" content="{BASE}/assets/img/recruit-division-{d['slug']}-hero.jpg">
<link rel="alternate" hreflang="ja" href="{BASE}/recruit/division/{d['slug']}.html"><link rel="alternate" hreflang="en" href="{BASE}/recruit/en/division/{d['slug']}.html">
</head>
<body>
<header class="header header--solid" id="header">
  <a href="../../../en/index.html" class="header__logo">
    <img src="../../../assets/logo/cj-logo-white-text.svg" alt="" class="header__logo-white" aria-hidden="true">
    <img src="../../../assets/logo/cj-logo-black-text.svg" alt="Custom Japan Co., Ltd." class="header__logo-color">
  </a>
  <nav class="header__nav">
{nav}
    <a href="../../division/{d['slug']}.html" class="header__lang">日本語</a>
    <a href="../index.html#entry" class="header__recruit"><span class="header__recruit-en">ENTRY</span><span class="header__recruit-jp">Apply</span></a>
  </nav>
  <button class="header__menu-btn" id="menuBtn" aria-controls="mobileMenu" aria-expanded="false" aria-label="Menu"><span></span><span></span></button>
</header>
<div class="mobile-menu" id="mobileMenu"><nav>
{nav}
    <a href="../../division/{d['slug']}.html">日本語</a>
    <a href="../index.html#entry" class="mobile-menu__recruit">ENTRY — Apply</a>
</nav></div>
<button class="mascot-top" id="mascotTop" aria-label="Back to top"><img src="../../../assets/logo/cj-mascot.svg" alt=""><span>TOP</span></button>
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
<div class="crumb"><a href="../../../en/index.html">Corporate</a><span>/</span><a href="../index.html">Careers</a><span>/</span>{d['jp']}</div>
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OVERVIEW</p>
    <p class="dv-lead reveal">{d['lead']}</p>
    <p class="dv-body reveal">{d['body']}</p>
    {gtag}
  </div>
</section>
<section class="page-section page-section--off">
  <div class="inner">
    <p class="sec-label reveal">WHAT MAKES IT EXCITING</p>
    <h2 class="sec-title sec-title--sm reveal">What makes this division exciting</h2>
    <div class="dv-missions">
{mission}
    </div>
  </div>
</section>
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">POSITIONS</p>
    <h2 class="sec-title sec-title--sm reveal">Open positions</h2>
    <div class="dv-positions">
{positions}
    </div>
    <p class="reveal" style="margin-top:36px"><a href="../index.html#entry" class="btn-solid">Apply to this division</a></p>
  </div>
</section>
<section class="page-section">
  <div class="inner">
    <p class="sec-label reveal">OTHER DIVISIONS</p>
    <h2 class="sec-title sec-title--sm reveal">See other divisions</h2>
    <div class="dv-others">
{others_html}
    </div>
  </div>
</section>
<footer class="footer">
  <div class="inner">
    <div class="footer__top">
      <div class="footer__company">
        <img src="../../../assets/logo/cj-logo-white-text.svg" alt="CUSTOM JAPAN" class="footer__logo">
        <p class="footer__address">Custom Japan Co., Ltd.<br>Nipponbashi Center Bldg. 6F, 2-9-16 Nipponbashi, Chuo-ku, Osaka 542-0073, Japan<br>Careers: recruit@customjapan.jp</p>
      </div>
      <nav class="footer__nav"><a href="../index.html">RECRUIT TOP</a><a href="../index.html#jobs">JOBS</a><a href="../index.html#people">PEOPLE</a><a href="../global.html">GLOBAL</a><a href="../../../en/index.html">Corporate</a></nav>
      <div class="footer__contact"><p>Apply here</p><a href="../index.html#entry" class="btn-line btn-line--light">Entry</a></div>
    </div>
    <p class="footer__copy">&copy; Custom Japan Co., Ltd. All Rights Reserved.</p>
  </div>
</footer>
</main>
<script src="../../../js/vendor/gsap.min.js"></script>
<script src="../../../js/vendor/ScrollTrigger.min.js"></script>
<script src="../../../js/vendor/lenis.min.js"></script>
<script src="../../../js/main.js"></script>
</body>
</html>'''
for d in DIVS:
    others = [o for o in DIVS if o["slug"] != d["slug"]]
    (OUT / "division" / f"{d['slug']}.html").write_text(div_page(d, others), encoding="utf-8")
    print("wrote", OUT / "division" / f"{d['slug']}.html")

print("--- done ---")
