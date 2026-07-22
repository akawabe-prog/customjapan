#!/usr/bin/env bash
# 新コーポレート/採用サイト一式(intern=TOP, corporate/ 配下)を
# intern/ フォルダとしてまとめ dist/intern.zip を生成する。
# 未リンク・未完成の smart/ と、未参照の data/、開発用ファイルは除外。
set -euo pipefail
cd "$(dirname "$0")/.."   # プロジェクトルート

STAGE="$(mktemp -d)/intern"
mkdir -p "$STAGE"

# ---- ルート直下のページ/スクリプト ----
PAGES=(
  index.html                 # TOP = インターンページ
  entry.html                  # 応募(本エントリー)フォーム
  casual.html                 # カジュアル面談フォーム
  intern-thanks.html
  intern-error.html
  intern-entry.php
  casual-entry.php
  intern-entry-config.local.php.example
)

# ---- 同梱ディレクトリ ----
DIRS=( corporate recruit en css js assets )

for f in "${PAGES[@]}"; do
  [ -f "$f" ] && cp "$f" "$STAGE/$f"
done
for d in "${DIRS[@]}"; do
  # DSC01101-optimized.jpg(未使用の巨大元データ)は除外
  [ -d "$d" ] && rsync -a --exclude '.DS_Store' --exclude 'DSC01101-optimized.jpg' "$d" "$STAGE/"
done

# ---- デプロイ手順メモ ----
cat > "$STAGE/README-deploy.txt" <<'TXT'
新コーポレート/採用サイト 配置手順
====================================
構成:
  /                → TOP（インターン採用ページ）= index.html
  /corporate/      → 会社サイト（about / business / brands / events / news / contact）
  /recruit/        → 採用サイト
  /en/             → 英語版
  /css /js /assets → 共有アセット

・この intern/ の中身を、公開したいルート直下にそのまま配置してください。
・エントリーフォーム送信は PHP が動くサーバーが必要です（intern-entry.php）。
  静的ホスト(GitHub Pages 等)では送信されません。
  宛先/SMTP を設定する場合は intern-entry-config.local.php.example を
  intern-entry-config.local.php にコピーして記入（未設定なら mb_send_mail で送信）。
・SRD5(スマートシリーズ)専用ページ(smart/)は未完成のため未同梱・未リンクです。
TXT

# ---- zip 生成 ----
mkdir -p dist
rm -f dist/intern.zip
( cd "$(dirname "$STAGE")" && zip -rq intern.zip intern )
mv "$(dirname "$STAGE")/intern.zip" dist/intern.zip
rm -rf "$(dirname "$STAGE")"

echo "built dist/intern.zip"
du -h dist/intern.zip | awk '{print "size:",$1}'
unzip -l dist/intern.zip | tail -1
