from pandas import read_csv
import numpy as np

# Load dữ liệu rượu vang trắng từ UCI
wine = read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv',
    delimiter=';'
)

# Lấy dữ liệu thuộc tính lưu vào wine_X
wine_X = wine.iloc[:, :-1]

# Lấy dữ liệu nhãn lưu vào wine_y
wine_y = wine.iloc[:, -1]

#In các nhãn trong cột quality
print("Labels:", np.unique(wine_y))

#In số lượng nhãn và số lượng dữ liệu
print("Number of classes:", len(np.unique(wine_y)))
print("Number of data:", len(wine_y))
print()

# Hiển thị 5 hàng dữ liệu mẫu của mỗi nhãn
for i in np.unique(wine_y):
    print(f"Sample data from class {i}:")
    print(wine_X[wine_y == i].head())
    print()

#  Chia dữ liệu thành 10 phần K-fold
from sklearn.model_selection import KFold, cross_val_predict

kf = KFold(n_splits=10, shuffle=True, random_state=42)

# In số lượng phần tử tập test và các nhãn của từng fold
for fold, (train_index, test_index) in enumerate(kf.split(wine_X), 1):
    y_test = wine_y.iloc[test_index]

    print("Fold:", fold)
    print("Training size:", len(train_index))
    print("Test size:", len(test_index))
    print("Labels in test:", np.unique(y_test))
    print()

# Xây dựng mô hình KNN với 9 láng giềng
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

model_KNN = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=9)
)

#Dự đoán theo K-fold: mỗi mẫu được dự đoán khi nằm trong tập test
y_pred_KNN = cross_val_predict(model_KNN, wine_X, wine_y, cv=kf)

#ánh giá độ chính xác tổng thể của KNN
from sklearn.metrics import accuracy_score, classification_report

acc_KNN = accuracy_score(wine_y, y_pred_KNN)

print("Accuracy of KNN: %.2f %%" % (100 * acc_KNN))
print("Classification report - KNN:")
print(classification_report(wine_y, y_pred_KNN, zero_division=0))

#in nhãn dự đoán và nhãn thực tế của 12 phần tử
# đầu tiên trong tập test của fold thứ nhất
train_index, test_index = next(kf.split(wine_X))

X_train = wine_X.iloc[train_index]
X_test = wine_X.iloc[test_index]
y_train = wine_y.iloc[train_index]
y_test = wine_y.iloc[test_index]

model_KNN.fit(X_train, y_train)
y_pred_12 = model_KNN.predict(X_test.iloc[:12])

print("Predicted labels:", y_pred_12)
print("Ground truth:", y_test.iloc[:12].to_numpy())
print("Accuracy of 12 test samples: %.2f %%" %
      (100 * accuracy_score(y_test.iloc[:12], y_pred_12)))
print()

#In ma trận nhầm lẫn của KNN trên toàn bộ dữ liệu
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

labels = np.unique(wine_y)

cm_KNN = confusion_matrix(wine_y, y_pred_KNN, labels=labels)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm_KNN,
    display_labels=labels
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - KNN")
plt.show()

# Xây dựng mô hình Naive Bayes
from sklearn.naive_bayes import GaussianNB

model_Bayes = GaussianNB()

y_pred_Bayes = cross_val_predict(model_Bayes, wine_X, wine_y, cv=kf)

# Đánh giá độ chính xác tổng thể của Naive Bayes
acc_Bayes = accuracy_score(wine_y, y_pred_Bayes)

print("Accuracy of Naive Bayes: %.2f %%" % (100 * acc_Bayes))
print("Classification report - Naive Bayes:")
print(classification_report(wine_y, y_pred_Bayes, zero_division=0))

#Hiển thị ma trận nhầm lẫn của Naive Bayes
cm_Bayes = confusion_matrix(wine_y, y_pred_Bayes, labels=labels)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm_Bayes,
    display_labels=labels
)

disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Naive Bayes")
plt.show()
