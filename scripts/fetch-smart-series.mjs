#!/usr/bin/env node
/**
 * SMART SERIES (SRD5) — Custom Japan API から "SRD5" 検索の商品と看板画像を取得
 * eXs 方式 (eXs-ReBranding 2/exs/assets/js) と同一フロー:
 *   1. api-i /init (Origin 必須) → guid/authorization/cid cookie
 *   2. api-a Algolia プロキシ → query="SRD5"
 *   3. img.customjapan.net … item.img.l(看板大) / item.img.s(サムネ)
 * 出力:
 *   data/raw/algolia-srd5.json           … 生レスポンス
 *   data/catalog-smart.json              … 正規化カタログ
 *   assets/img/smart/{id}/main.jpg       … 看板画像(大)
 *   assets/img/smart/{id}/thumb.jpg      … サムネ
 * 使い方: node scripts/fetch-smart-series.mjs
 */
import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const QUERY = 'SRD5';
const ORIGIN = 'https://www.customjapan.net';
const INIT_URL = 'https://api-i.customjapan.net/api/v1/init';
const ALGOLIA_URL = 'https://api-a.customjapan.net/1/indexes/*/queries';
const IMG_BASE = 'https://img.customjapan.net';

async function authenticate() {
  const res = await fetch(INIT_URL, { method: 'GET', headers: { Origin: ORIGIN, 'x-site': 'ec' } });
  if (!res.ok) throw new Error(`init failed: HTTP ${res.status}`);
  const setCookies = res.headers.getSetCookie?.() ?? [];
  const cookie = setCookies.map((c) => c.split(';')[0]).join('; ');
  if (!cookie.includes('guid=')) throw new Error('init: no auth cookies returned');
  console.log('✓ init OK');
  return cookie;
}

async function fetchHits(cookie) {
  const body = {
    requests: [{
      indexName: 'item',
      params: {
        query: QUERY,
        hitsPerPage: 50,
        attributesToHighlight: [],
      },
    }],
  };
  const res = await fetch(ALGOLIA_URL, {
    method: 'POST',
    headers: { Origin: ORIGIN, 'Content-Type': 'application/json', Cookie: cookie },
    body: JSON.stringify(body),
  });
  const json = await res.json();
  if (json.result === 'error') throw new Error(`algolia: ${JSON.stringify(json.errors)}`);
  const r = json.results[0];
  await mkdir(join(ROOT, 'data', 'raw'), { recursive: true });
  await writeFile(join(ROOT, 'data', 'raw', 'algolia-srd5.json'), JSON.stringify(json, null, 2));
  console.log(`✓ ${r.nbHits} 件ヒット (query="${QUERY}")`);
  return r.hits;
}

const imgUrl = (p) => (!p ? null : p.startsWith('http') ? p : `${IMG_BASE}${p}`);

function normalize(h) {
  const price = h.price?.regular?.pc ?? {};
  return {
    id: h.objectID,
    name: h.name ?? '',
    maker: h.maker?.nameMain ?? h.maker?.name ?? null,
    makerId: h.maker?.id ?? null,
    category: h.category?.name ?? null,
    price: { taxIn: price.taxIn ?? null, taxEx: price.taxEx ?? null },
    status: h.status ?? null,
    jan: h.jan ?? null,
    makerNo: h.makerNo?.origin ?? null,
    color: h.color?.main?.value ?? null,
    img: { s: imgUrl(h.img?.s), l: imgUrl(h.img?.l) },
    url: `https://www.customjapan.net/item/${h.objectID}`,
  };
}

async function downloadImage(url, dest) {
  if (!url) return false;
  const res = await fetch(url, { headers: { Origin: ORIGIN } });
  if (!res.ok) return false;
  const buf = Buffer.from(await res.arrayBuffer());
  if (buf.length < 1000) return false;
  await writeFile(dest, buf);
  return true;
}

const cookie = await authenticate();
const hits = await fetchHits(cookie);
const catalog = hits.map(normalize);

let ok = 0;
for (const p of catalog) {
  const dir = join(ROOT, 'assets', 'img', 'smart', p.id);
  await mkdir(dir, { recursive: true });
  const gotMain = await downloadImage(p.img.l || `${IMG_BASE}/items/${p.id}_1.jpg`, join(dir, 'main.jpg'));
  const gotThumb = await downloadImage(p.img.s || `${IMG_BASE}/items/${p.id}_s.jpg`, join(dir, 'thumb.jpg'));
  p.localMain = gotMain ? `assets/img/smart/${p.id}/main.jpg` : null;
  p.localThumb = gotThumb ? `assets/img/smart/${p.id}/thumb.jpg` : null;
  if (gotMain) ok++;
  console.log(`${gotMain ? '✓' : '✗'} ${p.id} ${p.name} ¥${p.price.taxIn ?? '-'}`);
}

await writeFile(join(ROOT, 'data', 'catalog-smart.json'), JSON.stringify(catalog, null, 2));
console.log(`\n完了: 看板画像 ${ok}/${catalog.length} 件DL → data/catalog-smart.json`);
