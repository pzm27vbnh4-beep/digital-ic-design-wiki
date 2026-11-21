# 邏輯合成（Logic Synthesis）與 Netlist

## 一句話白話定義
透過 EDA 工具，自動將工程師寫的 RTL 程式碼「翻譯」成由基本邏輯閘組成的電路網表（Netlist）。

## 生活比喻
邏輯合成就像是「硬體界的編譯器」，把建築師的功能設計圖，自動轉換成詳細的「建材清單與結構圖」（需要幾根鋼筋、幾塊磚頭）。

## 核心運作與關鍵名詞
- **三大輸入檔案**：
  1. **RTL 程式碼**：定義電路的功能邏輯。
  2. **標準元件庫（Standard Cell Library）**：由晶圓廠提供，裡面包含 AND、OR、Flip-Flop 等基本邏輯閘的實體特性。
  3. **時序約束檔（SDC）**：告訴工具這顆晶片必須跑多快等限制條件。
- **輸出成果 — Netlist（閘級電路網表）**：描述晶片裡用了哪些標準邏輯閘，以及它們彼此之間怎麼連接。
- **可測試性設計（DFT）**：在合成階段通常會一併加入測試電路，方便未來晶片製造完成後能快速篩檢出不良品。

## 上下游關聯
- 接收來自 [[spec-and-rtl]] 的程式碼，並透過 [[verification-and-simulation]] 中的形式驗證（Formal Verification）確保翻譯前後功能完全一致。
- 產出的 Netlist 是前端與後端的交接點，會直接交給 [[physical-design-pnr]] 進行實體擺放與繞線。

## 資料來源
- `raw/01_ic_flow_overview.md`
- `raw/02_frontend_rtl_and_eda.md`
- `raw/03_verification_and_sta.md`
