#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""社員インタビュー詳細ページ生成
data/interviews-full.json (旧サイトからの全文・Wayback復元) と
recruit/interviews-data.js (メタ情報・要約) から recruit/interview/iv*.html を生成する。
iv3 は旧記事(6769)が未アーカイブのため要約本文で構成。
"""
import json, re, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = json.load(open(f"{ROOT}/data/interviews-full.json", encoding="utf-8"))

# interviews-data.js からメタと要約を取得
src = open(f"{ROOT}/recruit/interviews-data.js", encoding="utf-8").read()
META = {}
for m in re.finditer(
    r'id:"(iv\d)", img:"([^"]*)", no:"([^"]*)", dept:"([^"]*)", meta:"([^"]*)",\s*'
    r'role:"([^"]*)",\s*title:"([^"]*)",\s*body:\[(.*?)\]', src, re.S):
    body = re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(8))
    META[m.group(1)] = dict(img=m.group(2), no=m.group(3), dept=m.group(4),
                            meta=m.group(5), role=m.group(6), title=m.group(7), body=body)

ORDER = ["iv1", "iv2", "iv3", "iv4", "iv5", "iv6", "iv7"]
esc = lambda s: html.escape(s, quote=True)

def page(slug):
    mt = META[slug]
    full = FULL.get(slug)
    idx = ORDER.index(slug)
    prev = ORDER[idx - 1] if idx > 0 else None
    nxt = ORDER[idx + 1] if idx < len(ORDER) - 1 else None

    # 本文: 全文があれば章構成、無ければ(iv3)要約段落
    if full:
        chapters = full["chapters"]
        schedule = full["schedule"]
    else:
        chapters = [{"h": "", "paras": mt["body"]}]
        schedule = []

    ch_html = ""
    for i, ch in enumerate(chapters, 1):
        if ch["h"]:
            ch_html += f'''
      <section class="ivp-chapter reveal">
        <h2><span>{i:02d}</span>{esc(ch["h"])}</h2>
        {''.join(f'<p>{esc(p)}</p>' for p in ch["paras"])}
      </section>'''
        else:
            ch_html += f'''
      <section class="ivp-chapter reveal">
        {''.join(f'<p>{esc(p)}</p>' for p in ch["paras"])}
      </section>'''

    sched_html = ""
    if schedule:
        items = "".join(
            f'<li><time>{esc(t)}</time><span>{esc(label)}</span></li>'
            for t, label in schedule)
        sched_html = f'''
      <section class="ivp-schedule reveal">
        <h2>1日のスケジュール</h2>
        <ul>{items}</ul>
      </section>'''

    nav = '<div class="ivp-nav reveal">'
    if prev:
        nav += f'<a href="{prev}.html" class="ivp-nav__link">← INTERVIEW {META[prev]["no"]}</a>'
    else:
        nav += '<span></span>'
    nav += '<a href="../index.html#people" class="ivp-nav__all">一覧へ戻る</a>'
    if nxt:
        nav += f'<a href="{nxt}.html" class="ivp-nav__link">INTERVIEW {META[nxt]["no"]} →</a>'
    else:
        nav += '<span></span>'
    nav += '</div>'

    note = ''
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>社員インタビュー {esc(mt["no"])} {esc(mt["title"])} | 採用情報 | 株式会社カスタムジャパン</title>
<meta name="description" content="{esc(mt["dept"])} {esc(mt["meta"])}のインタビュー。{esc(mt["title"])}">
<link rel="icon" href="../../assets/logo/cj-mascot.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;600;800&family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/style.css">
<style>
.ivp-hero{{display:grid;grid-template-columns:1fr 1.15fr;gap:clamp(28px,5vw,64px);align-items:center;max-width:1060px;margin:0 auto clamp(48px,8vh,84px)}}
.ivp-hero img{{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:18px}}
.ivp-hero__no{{font-family:var(--font-en);font-weight:800;font-size:12px;letter-spacing:.3em;color:var(--c-red);margin-bottom:14px}}
.ivp-hero h1{{font-size:clamp(22px,3vw,32px);font-weight:900;line-height:1.65;letter-spacing:.02em;margin-bottom:18px}}
.ivp-hero__meta{{font-size:13px;color:var(--c-gray);line-height:1.9}}
.ivp-hero__meta b{{color:var(--c-black);font-weight:700}}
@media(max-width:760px){{.ivp-hero{{grid-template-columns:1fr}}}}
.ivp-chapter{{max-width:760px;margin:0 auto clamp(40px,7vh,64px)}}
.ivp-chapter h2{{display:flex;gap:16px;align-items:baseline;font-size:clamp(17px,2.1vw,22px);font-weight:900;line-height:1.7;margin-bottom:18px}}
.ivp-chapter h2 span{{font-family:var(--font-en);font-weight:800;font-size:12px;letter-spacing:.18em;color:var(--c-red);flex-shrink:0}}
.ivp-chapter p{{font-size:14.5px;color:#3c4149;line-height:2.15;margin-bottom:1.2em}}
.ivp-schedule{{max-width:760px;margin:0 auto clamp(48px,8vh,84px);background:var(--c-off);border-radius:18px;padding:clamp(26px,4vw,44px)}}
.ivp-schedule h2{{font-size:16px;font-weight:900;letter-spacing:.06em;margin-bottom:22px}}
.ivp-schedule ul{{list-style:none;margin:0;padding:0}}
.ivp-schedule li{{display:flex;gap:18px;align-items:baseline;padding:10px 0;border-bottom:1px dashed var(--c-line)}}
.ivp-schedule li:last-child{{border-bottom:none}}
.ivp-schedule time{{font-family:var(--font-en);font-weight:800;font-size:13px;color:var(--c-red);min-width:3.4em}}
.ivp-schedule span{{font-size:13.5px;color:#3c4149}}
.ivp-nav{{max-width:760px;margin:0 auto 10vh;display:flex;justify-content:space-between;align-items:center;gap:14px;border-top:1px solid var(--c-line);padding-top:26px}}
.ivp-nav a{{font-size:12.5px;font-weight:700;color:var(--c-dark)}}
.ivp-nav a:hover{{color:var(--c-red)}}
.ivp-nav__all{{border:1px solid var(--c-line);border-radius:100px;padding:9px 22px}}
.ivp-cta{{max-width:760px;margin:0 auto 12vh;background:linear-gradient(120deg,var(--c-red),#8f1414);color:#fff;border-radius:20px;padding:clamp(30px,5vw,48px);text-align:center}}
.ivp-cta h2{{font-size:clamp(18px,2.4vw,24px);font-weight:900;margin-bottom:10px}}
.ivp-cta p{{font-size:12.5px;color:rgba(255,255,255,.85);margin-bottom:24px}}
.ivp-cta .btn-solid{{background:#fff;color:var(--c-red)}}
.reveal{{opacity:1}}
</style>
</head>
<body>

<header class="form-topbar">
  <a href="../../corporate/index.html" class="form-topbar__logo" aria-label="企業サイト"><img src="../../assets/logo/cj-logo-black-text.svg" alt="CUSTOM JAPAN"></a>
  <a href="../index.html#people" class="form-topbar__back">← 採用情報（働くひと）に戻る</a>
</header>

<main class="form-main" style="max-width:1100px">
  <div class="ivp-hero">
    <img src="../../assets/img/{esc(mt["img"])}" alt="{esc(mt["dept"])} {esc(mt["meta"])}">
    <div>
      <p class="ivp-hero__no">INTERVIEW {esc(mt["no"])}</p>
      <h1>{esc(mt["title"])}</h1>
      <p class="ivp-hero__meta"><b>{esc(mt["meta"])}</b><br>{esc(mt["dept"])}<br>{esc(mt["role"])}</p>
    </div>
  </div>
{ch_html}
{sched_html}
{nav}
  <div class="ivp-cta">
    <h2>一緒に働く仲間を、募集しています。</h2>
    <p>中途・新卒とも歓迎。まずは募集職種をご覧ください。</p>
    <a href="../entry.html" class="btn-solid">エントリーはこちら</a>
  </div>
{note}</main>
</body>
</html>
'''

os.makedirs(f"{ROOT}/recruit/interview", exist_ok=True)
for slug in ORDER:
    p = f"{ROOT}/recruit/interview/{slug}.html"
    open(p, "w", encoding="utf-8").write(page(slug))
    print("wrote", p)
print("done:", len(ORDER), "pages")
