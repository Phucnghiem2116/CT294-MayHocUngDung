import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('3.2.Housing/housing.csv', header=None, sep=r'\s+')
print(data.head())

# xác định các đặc trưng
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# chuẩn hóa
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled[:2])

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

#Xây dựng mô hình cây quyế định
regressor = DecisionTreeRegressor()
regressor.fit(X_scaled, y)
y_pred_reg = regressor.predict(X_scaled)
# Đánh giá mô hình cây quyết định hồi quy
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y, y_pred_reg)
r2 = r2_score(y, y_pred_reg)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')
# vẽ cây hồi quy
plt.figure(figsize=(12,8))
plot_tree(regressor, filled=True)
plt.show()