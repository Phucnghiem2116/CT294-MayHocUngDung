import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

#Đọc dữ liệu

# Danh sách 14 tên cột chuẩn của tập Boston Housing
column_names = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV',]

# Dùng header=None vì file không có tiêu đề, và r'\s+' để tách theo khoảng trắng
df = pd.read_csv(
    '3.4.Baitaplamthem/housing.csv', header=None, names=column_names, sep=r'\s+'
)
print(df.head())
#Phân tích dữ liệu
print('\n--- B. PHÂN TÍCH CẤU TRÚC DỮ LIỆU ---')
print(f'- Số lượng thuộc tính (cột): {df.shape[1]}')
print(f'- Số lượng phần tử (dòng): {df.shape[0]}')
print(f'- Tên các cột: {df.columns.tolist()}')
print(
    "- Cột nhãn mục tiêu (Target): 'MEDV' (Giá nhà trung bình dạng số thực"
    ' liên tục).\n')
# Tách x và y
X = df.drop(columns=['MEDV'])
y = df['MEDV']
# c, d, eVòng lặp 10 lần với Hold-out (70% train, 30% test)
#các giá trị random_state [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
random_states = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
r2_results = []
mse_results = []
print('--- C, D, E HUẤN LUYỆN VÀ ĐÁNH GIÁ QUA 10 LẦN LẶP ---')
for idx, rs in enumerate(random_states):
  # Chia tập dữ liệu 70% train, 30% test
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=rs)
  #  mô hình Decision Tree Regressor
  regressor = DecisionTreeRegressor(random_state=rs)
  regressor.fit(X_train, y_train)
  # Dự đoán test
  y_pred = regressor.predict(X_test)
  # Tính các độ đo đánh giá
  r2 = r2_score(y_test, y_pred)
  mse = mean_squared_error(y_test, y_pred)

  r2_results.append(r2)
  mse_results.append(mse)

  print(f'Lần {idx+1} (random_state={rs}) -> R^2 Score: {r2:.4f} | MSE:'f' {mse:.4f}')

  # Lưu và hiển thị kết quả cuố cùng
  if idx == len(random_states) - 1:
    print('\n[KẾT QUẢ LẦN LẶP CUỐI CÙNG]')
    print(f'Random State: {rs}')
    print(f'R^2 Score lần cuối: {r2:.4f}')
    print(f'MSE lần cuối: {mse:.4f}\n')
#Tính độ chính xác trung bình sau 10 lần lặp

avg_r2 = np.mean(r2_results)
avg_mse = np.mean(mse_results)
print('--- F. TỔNG KẾT VÀ SO SÁNH ---')
print(f'Độ chính xác trung bình (R^2) sau 10 lần lặp: {avg_r2:.4f}')
print(f'Sai số trung bình (MSE) sau 10 lần lặp: {avg_mse:.4f}')
print(
    '\n- So sánh với Naive Bayes hồi quy: Mô hình Decision Tree Regressor'
    ' thường mang lại độ chính xác (R^2) cao hơn so với Naive Bayes trên tập'
    ' dữ liệu Boston Housing. Lý do là vì Decision Tree xử lý tốt các mối quan'
    ' hệ phi tuyến tính phức tạp giữa các đặc trưng (như diện tích, vị trí,'
    ' tội phạm,...) và giá nhà, trong khi Naive Bayes chịu ràng buộc bởi giả'
    ' định các thuộc tính phải độc lập tuyến tính với nhau (điều ít khi đúng'
    ' trong dữ liệu thực tế).'
)