# Raw 01：從 RTL 到 GDSII — 數位 IC 設計完整流程鳥瞰
- **來源**：優半導體 Uedu Semiconductor — https://uedu.tw/semiconductor/a/eda-flow
- **主題**：數位 IC 設計全流程、前後端分工、PPA 目標

## 核心內容
數位 IC 設計是將抽象的系統功能需求，一步步轉換為晶圓代工廠（Foundry）能製造的實體光罩版圖（GDSII）的過程。整體流程通常分為「前端設計（Front-end）」與「後端設計（Back-end）」兩大階段。

1. **前端設計（Front-end）**：
   - 從系統規格（Specification）出發，工程師使用硬體描述語言（如 Verilog、VHDL）撰寫暫存器傳輸級程式碼（RTL）。
   - 接著進行大量的功能驗證（Verification），確保邏輯行為完全符合規格。
   - 驗證通過後，透過「邏輯合成（Logic Synthesis）」工具，將 RTL 程式碼轉換成由標準邏輯閘（Standard Cells）組成的閘級電路網表（Gate-level Netlist）。
   - 同時會加入可測試性設計（DFT, Design for Testability），方便晶片製造出來後進行測試。

2. **後端設計（Back-end / Physical Design）**：
   - 拿到 Netlist 後，進入實體設計階段，包含平面規劃（Floorplan）、擺放元件（Placement）、時脈樹合成（CTS）與繞線（Routing）。
   - 最後必須通過嚴格的簽核（Signoff）檢查，包含靜態時序分析（STA）、設計規則檢查（DRC）、佈局與電路圖一致性檢查（LVS）以及壓降分析（IR Drop）。
   - 所有檢查過關後，輸出最終的 **GDSII** 檔案送交晶圓廠製造（稱為 Tape-out）。

3. **貫穿全流程的核心指標 — PPA**：
   - 整個設計過程都在追求 **PPA（Performance 效能、Power 功耗、Area 面積）** 的最佳平衡。
