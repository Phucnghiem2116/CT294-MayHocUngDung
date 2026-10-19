from pandas import read_csv
import numpy as np

# 1. Load dữ liệu Iris từ file CSV
iris = read_csv('Iris.csv', delimiter=',', index_col=0)

# 2. Lấy dữ liệu thuộc tính lưu vào data_X
iris_X = iris.iloc[:, :-1]

# 3. Lấy dữ liệu nhãn lưu vào data_y
iris_y = iris.iloc[:, -1]

# print các nhãn trong cột Target
print(iris.iloc[:, -1].unique())

# 4. Chuyển đổi dữ liệu nhãn thành dạng số
iris_y = iris_y.map({'Setosa': 0, 'Versicolor': 1, 'Virginica': 2})

# 5. In các thông tin về nhãn và số lượng dữ liệu
print("Number of classes: ", len(np.unique(iris_y)))
print("Number of data: ", len(iris_y))
print()

# 6. Hiển thị 5 hàng dữ liệu mẫu của mỗi nhãn
for i in range(3):
    print(f"Sample data from class {i}:")
    print(iris_X[iris_y == i].head())
    print()

# Naive Bayes using load dataset from library
from sklearn.model_selection import train_test_split
# Phân chia tập dataset
X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=50)

print("Training size: %d" % len(y_train))
print("Test size    : %d" % len(y_test))
print(y_test)


from sklearn.naive_bayes import GaussianNB
# Huấn luyện mô hình Bayes thơ ngây
model_Bayes = GaussianNB()
model_Bayes.fit(X_train, y_train)
# Dự đoán kết quả trả về từ tập test
y_pred = model_Bayes.predict(X_test)
# Hiển thị kết quả của 20 dữ liệu test
print("Print results for 20 test data points:")
print("Predicted labels: ", y_pred[0:20])
print("Ground truth    : ", y_test[0:20])

from sklearn.metrics import accuracy_score
#tính độ chính xác tổng thể
print("Accuracy of Bayes thơ ngây: %.2f %%" % (100 * accuracy_score(y_test, y_pred)))

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. Tính toán ma trận nhầm lẫn: so sánh thực tế và dự đoán
cm = confusion_matrix(y_test, y_pred)

# 2. Hiển thị ma trận
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Setosa', 'Versicolor', 'Virginica'])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Naive Bayes")
plt.show()