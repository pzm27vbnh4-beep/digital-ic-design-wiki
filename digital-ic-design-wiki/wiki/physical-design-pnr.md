# 後端實體設計與佈局繞線（Physical Design / APR）

## 一句話白話定義
將前端產出的邏輯閘網表（Netlist），真正「擺放」進指甲大小的矽晶片空間並用多層金屬線全部接通的過程。

## 生活比喻
就像蓋智慧大樓時的「基地規劃與水電配管」：先決定地基大小與機房位置（Floorplan）、安排各個房間（Placement），最後拉設全棟不打架的水管、電線與網路線（Routing）。

## 核心運作與關鍵名詞
這個階段常稱為 **APR（自動佈局繞線，Auto Place and Route）**，包含四大核心步驟：
- **平面規劃（Floorplan）**：決定晶片總面積、輸入輸出腳位（I/O Pin）位置、固定大型記憶體（SRAM）區域，並規劃供電網路（Power Grid）。
- **元件擺放（Placement）**：由 EDA 工具自動擺放數百萬個標準邏輯閘。核心原則是「常互相溝通的元件放近一點」，以縮短連線、降低延遲與擁塞。
- **時脈樹合成（CTS, Clock Tree Synthesis）**：建立平衡的時脈分配樹，讓時脈訊號像樂團指揮一樣**幾乎同時**抵達每個暫存器，減少時間差（Clock Skew）。
- **繞線（Routing）**：利用多層金屬導線依 Netlist 連接所有元件，同時避免導線過近造成訊號干擾（Crosstalk）。

## 上下游關聯
- 承接來自 [[logic-synthesis]] 產出的閘級網表（Netlist）。
- 繞線完成後進入 [[signoff-and-tapeout]]；若後續檢查發現時序違規，必須**反覆迭代（Iteration）**退回重新擺放、重新合成，甚至修改 [[spec-and-rtl]]。
- 擺放與繞線的緊密程度直接影響晶片面積、速度與散熱，詳見 [[ppa-tradeoff]]。

## 資料來源
- `raw/01_ic_flow_overview.md`
- `raw/04_backend_pnr_and_signoff.md`
- `raw/05_analogy_and_tapeout.md`
