# main_pipeline.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# 1. 配置
DATA_PATH = 'data/sms_spam_no_header.csv'
MODEL_PATH = 'model/spam_classifier_mnb.pkl'
VECTORIZER_PATH = 'model/tfidf_vectorizer.pkl'

# 2. 數據載入
df = pd.read_csv(DATA_PATH, encoding='latin-1', header=None)

# 修正：由於沒有標頭，Pandas 使用 0, 1, ... 作為欄位名。
# 根據原始資料集，第 0 欄是標籤，第 1 欄是文本。
# 我們將欄位名稱 0 和 1 重新命名為 'label' 和 'text'。
df = df.rename(columns={0: 'label', 1: 'text'})
# 接著只選取這兩個需要的欄位（如果檔案中有多餘的空欄位，這個步驟是必要的）
df = df[['label', 'text']]

df['label'] = df['label'].map({'ham': 0, 'spam': 1}) # 保持不變

# 3. 數據預處理與向量化
X = df['text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用 TF-IDF 進行向量化
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# 4. 模型訓練 (Multinomial Naive Bayes)
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# 5. 評估
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 6. 結果輸出
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print("\nConfusion Matrix:")
print(cm)

# 7. 模型和 Vectorizer 保存
import os
os.makedirs('model', exist_ok=True)
joblib.dump(model, MODEL_PATH)
joblib.dump(tfidf_vectorizer, VECTORIZER_PATH)

print("\n模型和 Vectorizer 已成功保存到 'model/' 資料夾。")