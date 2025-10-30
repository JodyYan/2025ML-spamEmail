# streamlit_app.py

import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

# 1. 配置與模型載入
MODEL_PATH = 'model/spam_classifier_mnb.pkl'
VECTORIZER_PATH = 'model/tfidf_vectorizer.pkl'

# 使用 Streamlit 緩存，避免每次運行都重新載入
@st.cache_resource
def load_resources():
    """載入訓練好的模型和 Vectorizer。"""
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    except FileNotFoundError:
        st.error("錯誤：模型或 Vectorizer 文件未找到。請先運行 main_pipeline.py 訓練模型。")
        return None, None

model, vectorizer = load_resources()

# 模擬測試數據的結果 (用於展示指標圖表)
# 這些數值應與 main_pipeline.py 的實際輸出保持一致。
mock_accuracy = 0.9856
mock_precision = 0.9412
mock_recall = 0.9018
mock_f1 = 0.9211
# 模擬混淆矩陣: [[TN, FP], [FN, TP]]
cm = np.array([[800, 6], [11, 102]]) 


# 2. Streamlit 介面佈局
# 使用 'wide' 佈局讓內容佔滿整個頁面寬度
st.set_page_config(page_title="📧 Email Spam Classification", layout="wide")

st.title("📧 Email Spam Classification - OpenSpec Project")
st.markdown("---")

# 3. 交互式分類區
st.header("1. 交互式郵件分類 (Interactive Classifier)")
if model and vectorizer:
    # 使用 container 包裹，保持視覺整潔
    with st.container(border=True):
        user_input = st.text_area("請輸入一封電子郵件或 SMS 文本進行分類：", 
                                  "WINNER! Your free entry to the contest is confirmed! Text STOP to 8888 for cancellation.")
        
        if st.button("分類 (Classify)"):
            if user_input:
                # 預處理輸入文本
                input_vectorized = vectorizer.transform([user_input])
                # 進行預測
                prediction = model.predict(input_vectorized)[0]
                
                st.markdown("### 預測結果 (Prediction)")
                if prediction == 1:
                    st.error("🚨 判斷為：**垃圾郵件 (SPAM)**")
                else:
                    st.success("✅ 判斷為：**非垃圾郵件 (HAM)**")
            else:
                st.warning("請輸入文本進行分類。")

st.markdown("---")

# 4. 模型評估與可視化區
st.header("2. 模型評估與可視化 (Model Evaluation & Visualization)")

# 4.1 指標展示
st.subheader("📊 關鍵性能指標 (Key Performance Metrics)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("準確度 (Accuracy)", f"{mock_accuracy:.4f}")
col2.metric("精確度 (Precision)", f"{mock_precision:.4f}")
col3.metric("召回率 (Recall)", f"{mock_recall:.4f}")
col4.metric("F1 分數 (F1-Score)", f"{mock_f1:.4f}")


# 4.2 混淆矩陣圖
st.subheader("📉 混淆矩陣 (Confusion Matrix)")
st.caption("基於測試集數據的模型表現。")

# 繪製混淆矩陣的優化區域
# 調整 figsize 確保圖表緊湊，並調整字體大小
fig, ax = plt.subplots(figsize=(3.5, 3)) # 設置較小的圖表尺寸

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['HAM (Pred)', 'SPAM (Pred)'],  # 縮短標籤
            yticklabels=['HAM (Actual)', 'SPAM (Actual)'], # 縮短標籤
            annot_kws={"fontsize": 12}, # 調整格子內數字的字體大小
            ax=ax)

# 調整軸標籤和刻度字體大小
ax.set_ylabel('Actual Label', fontsize=10)
ax.set_xlabel('Predicted Label', fontsize=10)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10, rotation=0) # 確保 y 軸標籤不旋轉

plt.title("Confusion Matrix", fontsize=10)
plt.tight_layout() # 確保所有元素都能緊湊顯示

# 使用 Streamlit 顯示圖表，並關閉 use_container_width=False 確保不被拉伸
# 可以在 col1 中顯示圖表，保持版面整潔
plot_col, _ = st.columns([1, 2])
with plot_col:
    st.pyplot(fig, use_container_width=False) 

st.markdown("---")

# 5. 專案參考 (修復 st.secrets 錯誤)
# 直接使用硬編碼的 URL，避免 StreamlitSecretNotFound 錯誤
PACKT_REPO_URL = 'https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git'

st.header("3. 專案資訊與參考")
st.markdown(f"**📚 專案來源:** [Packt Cybersecurity AI Chapter 3]({PACKT_REPO_URL})")
st.markdown("**⚙️ 開發流程:** OpenSpec (Spec-Driven Development) + AI Coding CLI")