# LLM Wiki 操作與檢查紀錄（Log）

## [2026-11-21] INIT — 先討論、後生成
- **動作**：與 AI 討論並確認主題為「數位 IC 設計流程入門（RTL to GDSII）」。
- **產出**：建立 `AGENTS.md`、初始化 `index.md` 與 `log.md`，並備妥 5 篇 `raw/` 原始資料。
- **狀態**：✅ 準備進入 Ingest Loop（分兩輪處理 `raw/01` ~ `raw/05`）。

## [2026-11-21] INGEST ROUND 1 — 處理 `raw/01` ~ `raw/03`
- **動作**：依序 Ingest `raw/01_ic_flow_overview.md`、`raw/02_frontend_rtl_and_eda.md`、`raw/03_verification_and_sta.md`。
- **產出**：建立 `ic-design-overview.md`、`spec-and-rtl.md`、`verification-and-simulation.md`、`logic-synthesis.md`，並同步更新 `index.md`。
- **程式與品質檢查結果（攔截錯誤）**：
  - ✅ 禁止幻覺：所有數據（驗證佔 50~70%、人力比 2~3:1）皆明確出自 `raw/01~03`。
  - ❌ **發現問題（待第二輪修正）**：
    1. 出現 3 個尚未建立的斷鏈（`[[physical-design-pnr]]`、`[[signoff-and-tapeout]]`、`[[ppa-tradeoff]]`）。
    2. `ic-design-overview.md` 與 `spec-and-rtl.md` 的生活比喻尚未與第 5 篇「蓋智慧大樓」主軸統一。

## [2026-11-21] INGEST ROUND 2 — 處理 `raw/04` ~ `raw/05` 與最終檢查
- **動作**：Ingest `raw/04_backend_pnr_and_signoff.md` 與 `raw/05_analogy_and_tapeout.md`，新增 3 篇後端與 PPA 概念頁，並回頭統一 `ic-design-overview.md` 與 `spec-and-rtl.md` 的「蓋智慧大樓」比喻。
- **程式檢查結果（`python check.py`）**：
  - ✅ Wiki 概念頁數量：7 篇（PASS）
  - ✅ Wiki 交叉連結檢查：0 斷鏈（PASS）
  - ✅ 同步更新：`index.md` 7/7 完成（PASS）

## [2026-11-21] SLIDES — 規劃大綱與生成教學 HTML 簡報
- **動作**：讀取 `index.md` 產出 `slides/outline.md` 經人工確認後，渲染 9 頁互動式 `slides/index.html` 並產出 `slides/report.md`。
- **程式檢查結果（`python check.py`）**：
  - ✅ HTML 簡報頁數：9 頁（符合 8～15 頁規範）
  - ✅ HTML 簡報出處標註：9/9 頁皆標註對應 `Wiki 來源`
- **狀態**：✅ 全數 PASS，可進行獨立新對話 AI 審查與交件。
