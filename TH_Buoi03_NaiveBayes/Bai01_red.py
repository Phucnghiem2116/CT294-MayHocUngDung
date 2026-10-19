
from pandas import read_csv
import numpy as np

#Load dữ liệu Wine Quality từ link
wine = read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv',
    delimiter=';'
)

#lấy dữ liệu thuộc tính lưu vào data_X
wine_X = wine.iloc[:, :-1]

#ấy dữ liệu nhãn lưu vào data_y
wine_y = wine.iloc[:, -1]

#In các nhãn trong cột quality
print("Labels:", wine_y.unique())

#In số lượng nhãn và số lượng dữ liệu
print("Number of classes:", len(np.unique(wine_y)))
print("Number of data:", len(wine_y))
print()

# Hiển thị 5 hàng dữ liệu mẫu của mỗi nhãn
for i in np.unique(wine_y):
    print(f"Sample data from class {i}:")
    print(wine_X[wine_y == i].head())
    print()

#Phân chia dữ liệu theo tỷ lệ 4:1
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    wine_X, wine_y, test_size=0.2, random_state=42
)

print("Training size:", len(y_train))
print("Test size:", len(y_test))
print("Labels in test:", np.unique(y_test))
print("Number of different labels in test:", len(np.unique(y_test)))
print()

#Xây dựng mô hình Naive Bayes
from sklearn.naive_bayes import GaussianNB

model_Bayes = GaussianNB()
model_Bayes.fit(X_train, y_train)

# 9. Dự đoán kết quả từ tập test
y_pred_Bayes = model_Bayes.predict(X_test)

print("Predicted labels:", y_pred_Bayes[0:20])
print("Ground truth:", y_test.iloc[0:20].to_numpy())
print()

#Tính độ chính xác tổng thể
from sklearn.metrics import accuracy_score

acc_Bayes = accuracy_score(y_test, y_pred_Bayes)

print("Accuracy of Naive Bayes: %.2f %%" % (100 * acc_Bayes))

# Tính độ chính xác cho từng phân lớp
from sklearn.metrics import classification_report

print("Classification report - Naive Bayes:")
print(classification_report(y_test, y_pred_Bayes, zero_division=0))

# Hiển thị ma trận nhầm lẫn
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

labels = np.unique(wine_y)
cm = confusion_matrix(y_test, y_pred_Bayes, labels=labels)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=labels
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Naive Bayes")
plt.show()

#Xây dựng mô hình KNN để so sánh
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model_KNN = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=9)
)

model_KNN.fit(X_train, y_train)
y_pred_KNN = model_KNN.predict(X_test)

acc_KNN = accuracy_score(y_test, y_pred_KNN)

print("Accuracy of KNN: %.2f %%" % (100 * acc_KNN))
print("Accuracy of Naive Bayes: %.2f %%" % (100 * acc_Bayes))

#So sánh độ chính xác của hai mô hình
if acc_KNN > acc_Bayes:
    print("KNN has higher accuracy than Naive Bayes.")
elif acc_KNN < acc_Bayes:
    print("Naive Bayes has higher accuracy than KNN.")
else:
    print("Both models have the same accuracy.")
