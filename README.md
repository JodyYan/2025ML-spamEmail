# 📧 2025ML-spamEmail：電子郵件垃圾郵件分類專案

## 💡 專案簡介 (Project Overview)

本專案旨在實作一個高效的電子郵件垃圾郵件分類器，它是對 Packt Publishing《Hands-On Artificial Intelligence for Cybersecurity》第三章的**擴展和優化**。

我們嚴格遵循 **OpenSpec 規範驅動開發 (Spec-Driven Development)** 工作流程，並整合了 Streamlit 進行豐富的視覺化和交互式演示。

* **專案類型：** 電子郵件/SMS 文本分類 (二元分類)
* **模型:** Multinomial Naive Bayes (MNB)
* **特徵工程:** TF-IDF Vectorization
* **前端:** Streamlit

## ⚙️ 環境設定 (Project Setup)

### 前提條件

* Python 3.9+
* Node.js (如果需要使用 OpenSpec CLI)

### 1. 複製儲存庫與準備資料

```bash
git clone [https://github.com/huanchen1107/2025ML-spamEmail.git](https://github.com/huanchen1107/2025ML-spamEmail.git)
cd 2025ML-spamEmail
# 確保資料集 'sms_spam_no_header.csv' 放置在 ./data/ 資料夾中。
```
### 2. 安裝依賴套件
```bash
pip install -r requirements.txt
```
## 🚀 專案運行與展示 (Usage and Demo)
### 1. 訓練模型與保存資源運行核心 
ML Pipeline 以訓練模型、計算指標，並將訓練好的模型和 Vectorizer 保存到 ./model 資料夾：Bashpython main_pipeline.py
執行成功後，會在 ./model 資料夾下生成 spam_classifier_mnb.pkl 和 tfidf_vectorizer.pkl。
### 2. 啟動 Streamlit 
演示在本地啟動交互式分類器和視覺化介面：
```bash
streamlit run streamlit_app.py
```
應用程式將在您的瀏覽器中打開，請訪問 http://localhost:8501 進行交互測試。


## 📜 OpenSpec 工作流軌跡本專案的開發過程嚴格遵循 
OpenSpec 規範驅動流程：專案環境建構： 填充 openspec/project.md。變更提案創建： 針對 ML Pipeline 和 Streamlit UI 建立提案 (openspec/proposal.md, openspec/tasks.md)。實施與歸檔： 執行 AI 實現程式碼，並使用 openspec archive 命令將變更歷史歸檔。
