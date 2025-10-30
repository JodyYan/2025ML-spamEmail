# 專案規範 (Project Specification)

## 🎯 目的 (Goal)
使用機器學習模型對電子郵件/SMS 文本進行分類，判斷其是否為垃圾郵件（Spam）。專案將遵循 OpenSpec 規範驅動開發流程，並擴展 Packt 書籍 Chapter 3 的實作，增加豐富的可視化和 Streamlit 交互式前端。

## ⚙️ 技術棧 (Tech Stack)
* **語言:** Python 3.9+
* **ML 庫:** scikit-learn
* **數據處理/分析:** pandas, numpy
* **文本處理:** nltk
* **可視化:** matplotlib, seaborn
* **前端:** Streamlit
* **規範驅動:** OpenSpec + AI Coding CLI

## 📂 架構 (Architecture)
專案採用模組化架構：
1.  **`main_pipeline.py`:** 包含數據載入、預處理、模型訓練、評估和模型保存的核心邏輯。
2.  **`streamlit_app.py`:** 負責載入訓練好的模型，提供交互式的文本輸入介面和結果展示。
3.  **`data/`:** 存放原始資料集。

## 🖋️ 編碼風格與慣例 (Conventions)
* 使用 PEP 8 規範。
* 所有函式應包含 Docstrings 說明。
* 變數和函式名稱使用 `snake_case`。