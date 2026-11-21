import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
WIKI_DIR = ROOT / "wiki"
INDEX_FILE = ROOT / "index.md"
SLIDES_FILE = ROOT / "slides" / "index.html"

errors = []
warnings = []

print("=== 執行 LLM Wiki & HTML 簡報自動化檢查 (check.py) ===\n")

wiki_files = sorted(WIKI_DIR.glob("*.md"))
wiki_stems = {f.stem for f in wiki_files}

if len(wiki_files) < 5:
    errors.append(f"[Wiki 數量不足] 目前僅 {len(wiki_files)} 篇，至少需 5 篇以上概念頁。")
else:
    print(f"[PASS] Wiki 概念頁數量：{len(wiki_files)} 篇")

index_content = INDEX_FILE.read_text(encoding="utf-8") if INDEX_FILE.exists() else ""

for wf in wiki_files:
    text = wf.read_text(encoding="utf-8")
    if wf.name not in index_content:
        errors.append(f"[index.md 漏更] {wf.name} 未出現在 index.md 中。")
    if "raw/" not in text:
        errors.append(f"[缺少來源] {wf.name} 未標註 raw/ 資料來源。")
    links = re.findall(r"\[\[([^\]]+)\]\]", text)
    if len(set(links)) < 2:
        warnings.append(f"[連結偏少] {wf.name} 僅有 {len(set(links))} 個交叉連結（建議 >= 2）。")
    for link in links:
        target = link.replace(".md", "").strip()
        if target not in wiki_stems:
            errors.append(f"[斷鏈] {wf.name} 引用了不存在的頁面 [[{link}]]。")

if not any("[斷鏈]" in e for e in errors):
    print("[PASS] Wiki 交叉連結檢查：0 斷鏈")

if not SLIDES_FILE.exists():
    errors.append(f"[缺少簡報] 找不到 {SLIDES_FILE}。")
else:
    html = SLIDES_FILE.read_text(encoding="utf-8")
    slides = re.findall(r'<section[^>]*class="[^"]*slide[^"]*"[^>]*>.*?</section>', html, re.S)
    slide_count = len(slides)
    if not (8 <= slide_count <= 15):
        errors.append(f"[頁數不符] 目前簡報為 {slide_count} 頁，規範須為 8～15 頁。")
    else:
        print(f"[PASS] HTML 簡報頁數：{slide_count} 頁（符合 8～15 頁規範）")

    missing_source_pages = []
    for idx, s in enumerate(slides, start=1):
        if "Wiki 來源" not in s and "wiki/" not in s and ".md" not in s:
            missing_source_pages.append(idx)
    if missing_source_pages:
        errors.append(f"[簡報缺出處] 第 {missing_source_pages} 頁缺少 Wiki 來源標註。")
    else:
        print("[PASS] HTML 簡報出處標註：每一頁皆有標註對應 Wiki 來源")

print("\n=== 檢查結果彙總 ===")
for w in warnings:
    print("WARN :", w)
for e in errors:
    print("FAIL :", e)

if errors:
    print(f"\n❌ 檢查未通過，共發現 {len(errors)} 項錯誤，請依退回路線修正後重跑。")
    sys.exit(1)
else:
    print("\n✅ 所有程式檢查項目全數 PASS！可進入獨立新對話 AI 審查與交件。")
    sys.exit(0)
