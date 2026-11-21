# 規格制定（Spec）與 RTL 設計

## 一句話白話定義
先定好晶片要達成的功能與速度目標（Spec），再用硬體描述語言（RTL）寫出電路的邏輯運作方式。

## 生活比喻
Spec 像業主開出「10 層樓、耐震、預算 1 億」的需求；RTL 像建築師畫出功能設計圖，定義各樓層與電梯怎麼同時並發運作（而非像軟體一行一行排隊執行）。

## 核心運作與關鍵名詞
- **規格制定（Specification）**：晶片設計的第一步，定義運算速度（頻率）、功耗上限、晶片面積預算、支援的介面協議與成本目標。
- **RTL（Register Transfer Level，暫存器傳輸級）**：工程師使用 **Verilog** 或 **SystemVerilog** 等硬體描述語言，描述資料如何在暫存器之間流動與運算。
- **硬體描述 vs. 軟體程式**：
  - 軟體（如 Python/C）是「循序執行」，一行接一行跑。
  - 硬體（RTL）描述的是真實存在的電路元件，所有電路都是「**同時並發（Parallel）**」運作的；寫錯一行程式碼，可能代表多出幾千個電晶體或造成電路短路。

## 上下游關聯
- 本階段是 [[ic-design-overview]] 中「前端設計」的起點。
- 寫完 RTL 後，必須立刻進入 [[verification-and-simulation]] 確認邏輯無誤，再交由 [[logic-synthesis]] 翻譯成實體邏輯閘電路。

## 資料來源
- `raw/01_ic_flow_overview.md`
- `raw/02_frontend_rtl_and_eda.md`
- `raw/05_analogy_and_tapeout.md`
