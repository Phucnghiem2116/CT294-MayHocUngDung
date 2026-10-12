import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer


df = pd.read_csv("HousingData.csv")

print(df.head())
print(df.info())
print(df.columns)


print("\nSố dữ liệu bị thiếu:")
print(df.isnull().sum())


X = df.drop("MEDV", axis=1)
y = df["MEDV"]

#80% train-20% test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nSố dòng tập train:", len(X_train))
print("Số dòng tập test:", len(X_test))


imputer = SimpleImputer(strategy="mean")

X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nĐã chia và chuẩn hóa dữ liệu thành công!")



from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# Các giá trị k cần thử
k_values = [1, 3, 5, 7, 9]



print("KẾT QUẢ KNN TRƯỚC KHI CHUẨN HÓA")


for k in k_values:

    # Tạo mô hình KNN
    model = KNeighborsRegressor(n_neighbors=k)

   
    model.fit(X_train, y_train)

    
    y_pred = model.predict(X_test)

   
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print(f"\nk = {k}")
    print(f"MAE  = {mae:.4f}")
    print(f"MSE  = {mse:.4f}")
    print(f"RMSE = {rmse:.4f}")



print("KẾT QUẢ KNN SAU KHI CHUẨN HÓA")



for k in k_values:

    
    model = KNeighborsRegressor(n_neighbors=k)

    
    model.fit(X_train_scaled, y_train)

    
    y_pred = model.predict(X_test_scaled)

    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print(f"\nk = {k}")
    print(f"MAE  = {mae:.4f}")
    print(f"MSE  = {mse:.4f}")
    print(f"RMSE = {rmse:.4f}")