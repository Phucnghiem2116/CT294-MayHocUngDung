import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Đọc dữ liệu file excel
data = pd.read_excel("Play.xlsx", engine="openpyxl")

# Định nghĩa biến
X_data = data[['Weather', 'Temp']]
y_data = data['Play']

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2, random_state=42)

# Vì các biến đặc trưng là biến phân loại, ta cần mã hóa chúng thành dạng số trước khi huấn luyện mô hình
le = LabelEncoder()

for col in X_train.columns: # Với mỗi cột trong tập đặc trưng
    X_train[col] = le.fit_transform(X_train[col]) # Áp dụng Label Encoding cho tập huấn luyện
    X_test[col] = le.transform(X_test[col]) # Áp dụng Label Encoding cho tập kiểm tra dựa trên mã hóa của tập huấn luyện



model = DecisionTreeClassifier() # Tạo mô hình cây quyết định phân loại

model.fit(X_train, y_train) # Huấn luyện mô hình với tập huấn luyện
y_pred = model.predict(X_test) # Dự đoán trên tập kiểm tra


# Đánh giá mô hình

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Vẽ cây quyết định
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=X_data.columns, class_names=model.classes_, filled=True)
plt.show()