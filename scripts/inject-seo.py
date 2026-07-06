#!/usr/bin/env python3
"""全ページに OGP / Twitter Card / canonical / JSON-LD を注入(冪等)。
本番ドメインは BASE を変更。使い方: python3 scripts/inject-seo.py"""
import re, glob, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://customjapan.jp"   # ★本番ドメインに合わせて変更
DEFAULT_OG_IMG = BASE + "/assets/img/hero-rider.jpg"

def rel_to_url(p: Path):
    rel = p.relative_to(ROOT).as_posix()
    if rel == "index.html": return BASE + "/"
    if rel.endswith("/index.html"): return BASE + "/" + rel[:-len("index.html")]
    return BASE + "/" + rel

def og_image_for(rel):
    if rel.startswith("recruit"): return BASE + "/assets/img/recruit-work-catalog.jpg"
    return DEFAULT_OG_IMG

ORG_JSONLD = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"株式会社カスタムジャパン","alternateName":"Custom Japan Co., Ltd.","url":"%s/","logo":"%s/assets/logo/cj-logo-black-text.svg","foundingDate":"2005-08-09","address":{"@type":"PostalAddress","streetAddress":"日本橋2-9-16 日本橋センタービル6F","addressLocality":"大阪市中央区","addressRegion":"大阪府","postalCode":"542-0073","addressCountry":"JP"},"telephone":"+81-6-6563-9317","sameAs":["https://www.instagram.com/customjapan/","https://note.com/fair_auk890","https://prtimes.jp/main/html/searchrlp/company_id/70755"]}
</script>''' % (BASE, BASE)

files = glob.glob(str(ROOT/"*.html")) + glob.glob(str(ROOT/"en/*.html")) + glob.glob(str(ROOT/"recruit/*.html")) + glob.glob(str(ROOT/"recruit/division/*.html"))
for fp in files:
    p = Path(fp); src = p.read_text(encoding="utf-8")
    if "og:title" in src:  # 冪等
        continue
    rel = p.relative_to(ROOT).as_posix()
    title = re.search(r"<title>(.*?)</title>", src, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', src, re.S)
    title = title.group(1).strip() if title else "株式会社カスタムジャパン"
    desc = desc.group(1).strip() if desc else ""
    url = rel_to_url(p); ogimg = og_image_for(rel)
    lang = "en_US" if rel.startswith("en/") else "ja_JP"
    t = html.escape(title, quote=True); d = html.escape(desc, quote=True)
    block = f'''<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="株式会社カスタムジャパン">
<meta property="og:locale" content="{lang}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="{ogimg}">'''
    if rel in ("index.html", "recruit/index.html"):
        block += "\n" + ORG_JSONLD
    # in<head>末尾(</head>直前)に挿入
    src = src.replace("</head>", block + "\n</head>", 1)
    p.write_text(src, encoding="utf-8")
    print("seo+", rel)
