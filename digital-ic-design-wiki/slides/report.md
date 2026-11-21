# 數位 IC 設計入門簡報 — 獨立 AI 審查報告

## 1. 審查基本資訊
- **審查角色**：獨立 AI 審查員（全新對話無偏見評估）
- **唯一事實來源（Single Source of Truth）**：`wiki/` 內 7 篇概念頁（嚴格封閉檢驗）
- **審查目標物**：`slides/index.html`（共 9 頁投影片）
- **審查結果**：**✅ 全數通過（PASS）**

---

## 2. 覆蓋率審查（Coverage Audit）
審查 7 篇 Wiki 概念頁是否全數涵蓋於簡報中：

| Wiki 概念頁 | 對應簡報頁次 | 核心知識點涵蓋情形 | 判定 |
| :--- | :--- | :--- | :--- |
| `ic-design-overview.md` | P1, P2 | RTL to GDSII、蓋大樓比喻、前後端分工、EDA 角色、PPA 貫穿目標 | ✅ PASS |
| `spec-and-rtl.md` | P3, P9 | Spec 定義、Verilog/SystemVerilog、硬體並發 vs. 軟體循序、隨堂測驗 Q1 | ✅ PASS |
| `verification-and-simulation.md` | P4 | 50%～70% 工時、人力比 2:1～3:1、Testbench、覆蓋率、形式驗證、STA Setup/Hold Time | ✅ PASS |
| `logic-synthesis.md` | P5, P9 | 硬體界編譯器、三大輸入（RTL/標準元件庫/SDC）、Netlist 網表、DFT 電路、隨堂測驗 Q2 | ✅ PASS |
| `physical-design-pnr.md` | P6 | APR 四步驟（Floorplan/Placement/CTS/Routing）、Clock Skew、Crosstalk、迭代機制 | ✅ PASS |
| `signoff-and-tapeout.md` | P7, P9 | 四大簽核關卡（DRC/LVS/STA/IR Drop）、GDSII 實體版圖、Tape-out 流片、隨堂測驗 Q3 | ✅ PASS |
| `ppa-tradeoff.md` | P8 | PPA 三大指標互相牽制、手機（低功耗）/ AI 伺服器（效能）/ 家電（小面積）取捨模擬 | ✅ PASS |

- **覆蓋率結論**：**7 / 7 篇（100% 完整覆蓋）**，無任何遺漏。

---

## 3. 忠實度審查（Fidelity & Hallucination Audit）
針對各頁面內容進行忠實度、講反檢查與外部幻覺排查：

- **P1（封面與導覽）**：
  - 忠實度：明確定義前後端與大樓比喻，學習目標清楚。
  - 講反/幻覺：無講反，無幻覺。
- **P2（全流程鳥瞰）**：
  - 忠實度：前端（Spec/RTL/驗證/合成/DFT）與後端（APR/Signoff/Tape-out/GDSII/EDA）劃分完全吻合 `ic-design-overview.md`。
  - 講反/幻覺：無講反，無幻覺。
- **P3（Spec 規格與 RTL 設計）**：
  - 忠實度：精準對比軟體「循序執行（Sequential）」與硬體「同時並發（Parallel）」，以及寫錯程式碼的代價。
  - 講反/幻覺：觀念正確，無講反，無幻覺。
- **P4（功能驗證與模擬）**：
  - 忠實度：忠實呈現 Wiki 的關鍵數據區間「50%～70% 開發時間」與「2:1 甚至 3:1 人力比」；精確描述 Testbench、Coverage、形式驗證與 STA。
  - 講反/幻覺：數據與文字皆忠於原文，無硬湊或編造數據，無講反。
- **P5（邏輯合成與 Netlist）**：
  - 忠實度：清楚列出三大輸入（RTL、標準元件庫、SDC）與輸出 Netlist，並納入 DFT 與形式驗證。
  - 講反/幻覺：無講反，無幻覺。
- **P6（APR 實體佈局繞線）**：
  - 忠實度：互動元件準確對應 Floorplan（SRAM/IO/Power Grid）、Placement（互相溝通放近）、CTS（Clock Skew）、Routing（Crosstalk）四階段，並包含退回迭代機制。
  - 講反/幻覺：步驟與因果順序完全符合硬體實務與 Wiki 記載，無講反。
- **P7（簽核驗證 Signoff 與下線 Tape-out）**：
  - 忠實度：DRC（製造極限防短路斷路）、LVS（版圖與 Netlist 一致性）、STA（實體延遲時序收斂）、IR Drop（供電壓降）四大關卡定義精準，下線產出 GDSII。
  - 講反/幻覺：無講反，無幻覺。
- **P8（PPA 黃金三角與取捨模擬）**：
  - 忠實度：三大指標交互牽制原理解釋清楚，手機、AI 伺服器、家電三大情境之優先權重完全吻合 `ppa-tradeoff.md`。
  - 講反/幻覺：無講反，無幻覺。
- **P9（總結與隨堂測驗）**：
  - 忠實度：三道互動題目答案與解釋均依據 Wiki 核心概念出題，能精準驗收學習成效。
  - 講反/幻覺：無講反，無幻覺。

- **忠實度結論**：全片**零幻覺、零說法講反**，100% 忠於 `wiki/` 知識庫。

---

## 4. 程式檢查對齊（`python check.py`）
- `[PASS]` Wiki 概念頁數量：7 篇
- `[PASS]` Wiki 交叉連結檢查：0 斷鏈
- `[PASS]` HTML 簡報頁數：9 頁（落在 8～15 頁規範內）
- `[PASS]` HTML 簡報出處標註：P1～P9 每頁皆有 `Wiki 來源：` 標籤
- **Exit Code**：`0`

---

## 5. 審查總結
本 HTML 簡報完全恪守 `wiki/` 作為唯一事實來源的原則，不僅 100% 覆蓋全站 7 篇概念頁，且在專業概念（平行運作、Clock Skew、形式驗證、DRC/LVS）與生活比喻（智慧大樓）之間取得優秀的平衡，無任何自行編造的數據或顛倒事實，確認驗收合格。
