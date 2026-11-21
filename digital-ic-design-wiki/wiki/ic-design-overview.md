# 數位 IC 設計總覽（RTL to GDSII）

## 一句話白話定義
將抽象的晶片功能需求，透過軟體工具一步步轉換成晶圓廠能製造的實體電路藍圖（GDSII）的完整過程。

## 生活比喻
就像蓋一棟智慧大樓：前端負責業主需求、建築設計圖與 3D 防震模擬；後端負責基地規劃、水電配管、建管審查，最後交給營造廠動工。

## 核心運作與關鍵名詞
數位 IC 設計流程主要分為兩大階段：
- **前端設計（Front-end）**：負責「邏輯與功能」。包含制定規格（Spec）、撰寫 RTL 程式碼、功能驗證、邏輯合成（產出 Netlist）以及加入可測試性設計（DFT）。
- **後端設計（Back-end / Physical Design）**：負責「實體擺放與製造檢查」。拿到 Netlist 後，進行平面規劃（Floorplan）、擺放元件（Placement）、時脈樹合成（CTS）、繞線（Routing），最後通過簽核檢查（Signoff）輸出 **GDSII** 檔案送交晶圓代工廠（Foundry）。
- **EDA（電子設計自動化）**：現代晶片包含數十億顆電晶體，整個前後端流程都必須高度依賴 Synopsys、Cadence 等 EDA 軟體自動完成。
- **核心目標**：全流程都在追求 **PPA**（效能、功耗、面積）的最佳平衡。

## 上下游關聯
- 流程起點由 [[spec-and-rtl]] 開始，接著必須經過 [[verification-and-simulation]] 與 [[logic-synthesis]] 才能交棒給後端。
- 後端實體化與最終下線請見 [[physical-design-pnr]] 與 [[signoff-and-tapeout]]。
- 貫穿所有階段的權衡標準請見 [[ppa-tradeoff]]。

## 資料來源
- `raw/01_ic_flow_overview.md`
- `raw/02_frontend_rtl_and_eda.md`
- `raw/05_analogy_and_tapeout.md`
