# 數位 IC 設計流程入門 — Wiki 總目錄

> 本目錄於每次 Ingest 後由 AI 自動同步更新。共 7 篇概念頁，皆已通過 `check.py` 程式檢查。

| Wiki 頁面 | 核心主題 | 一句話摘要 | 狀態 | 來源資料 |
| :--- | :--- | :--- | :--- | :--- |
| `ic-design-overview.md` | 數位 IC 設計總覽 | 將抽象功能需求透過前後端流程轉為 GDSII 藍圖的全貌。 | ✅ 已完成 | `raw/01`, `raw/02`, `raw/05` |
| `spec-and-rtl.md` | 規格制定與 RTL 設計 | 定義晶片目標並用並發思維撰寫 Verilog 硬體描述語言。 | ✅ 已完成 | `raw/01`, `raw/02`, `raw/05` |
| `verification-and-simulation.md` | 功能驗證與模擬 | 佔開發 50~70% 時間，透過 Testbench、覆蓋率與 STA 防止天價 Bug。 | ✅ 已完成 | `raw/01`, `raw/03` |
| `logic-synthesis.md` | 邏輯合成與 Netlist | 結合標準元件庫與時序約束，將 RTL 翻譯為邏輯閘電路網表。 | ✅ 已完成 | `raw/01`, `raw/02`, `raw/03` |
| `physical-design-pnr.md` | 後端實體設計與佈局繞線 | 透過 Floorplan、Placement、CTS、Routing 將電路實體化。 | ✅ 已完成 | `raw/01`, `raw/04`, `raw/05` |
| `signoff-and-tapeout.md` | 簽核驗證與下線（Tape-out） | 通過 DRC、LVS、STA、IR Drop 檢查後輸出 GDSII 送晶圓廠製造。 | ✅ 已完成 | `raw/01`, `raw/04`, `raw/05` |
| `ppa-tradeoff.md` | 晶片設計黃金三角（PPA） | 效能、功耗、面積三者互相牽制，依應用場景決定取捨策略。 | ✅ 已完成 | `raw/01`, `raw/05` |
