# 簽核驗證（Signoff）與下線（Tape-out）

## 一句話白話定義
晶片送交晶圓廠量產前的最後一道物理與電氣總體檢，全部過關後輸出 GDSII 檔案正式動工（Tape-out）。

## 生活比喻
Signoff 就像政府建管處審查建築法規（牆壁夠不夠厚、管線有沒有照圖施工）；審查通過後把最終藍圖交給營造廠（如台積電）動工，就是 Tape-out。

## 核心運作與關鍵名詞
- **簽核驗證（Signoff）四大關卡**：
  - **DRC（設計規則檢查）**：檢查金屬線寬度與間距是否符合晶圓廠物理製造極限（太細會斷、太近會短路）。
  - **LVS（佈局與電路圖一致性檢查）**：確認畫出來的實體版圖跟原本的 Netlist 電路圖 100% 一致，沒有接錯線。
  - **STA（靜態時序分析）**：加上實際繞線延遲後，做最後一次時序收斂確認。
  - **IR Drop（壓降分析）**：確認供電網路能穩定把電壓送到晶片每個角落，避免局部電壓不足導致當機。
- **GDSII 與 Tape-out（流片 / 下線）**：所有 Signoff 檢查零錯誤後，輸出最終的 **GDSII** 實體光罩版圖檔案，送交晶圓代工廠（Foundry）正式製造。

## 上下游關聯
- 負責驗收 [[physical-design-pnr]] 的最終成果，並再次執行 [[verification-and-simulation]] 提到的 STA 檢查。
- 這是 [[ic-design-overview]] 的最後一關，任何檢查未過都必須退回上游進行反覆迭代。

## 資料來源
- `raw/01_ic_flow_overview.md`
- `raw/04_backend_pnr_and_signoff.md`
- `raw/05_analogy_and_tapeout.md`
