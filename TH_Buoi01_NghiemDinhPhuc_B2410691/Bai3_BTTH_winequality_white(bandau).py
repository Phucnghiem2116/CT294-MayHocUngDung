import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns


def calculate_per_class(con_matrix):
    accuracies = []
    for i in range(len(con_matrix)):
        correct_prediction = con_matrix[i][i]
        total_prediction = np.sum(con_matrix[i, :])

        if(total_prediction != 0):
            accuracy = (correct_prediction / total_prediction)
        else:
            accuracy = 0

        accuracies.append(accuracy)

    return accuracies


def print_data(x_data):
    for i in range(x_data.shape[1]):
        x = x_data.iloc[:, i]
        print("Du lieu cua thuoc tinh thu %d: " % (i + 1))
        print(x)
        print()

    print("-----------------------------\n")


# Doc du lieu
df = pd.read_csv("winequality-white.csv", sep=";")

t = df.shape

print("So hang du lieu: " + str(t[0]))
print("So cot du lieu: " + str(t[1]))
print("-----------------------------")
print()


# Phan tach du lieu
X_data = df.drop(["quality"], axis=1)
y_data = df["quality"]


# Lay cac gia tri cua nhan
labels = np.unique(y_data)

print("Tap cac gia tri cua nhan: ", labels)
print("-----------------------------")
print()


print_data(X_data)


# Chia tap du lieu:
# 8 phan dung de huan luyen
# 2 phan dung de kiem tra
X_train, X_test, y_train, y_test = train_test_split(
    X_data,
    y_data,
    test_size=0.2,
    random_state=42
)


# Thong tin tap test - Cau c
print("THONG TIN TAP TEST")
print("So luong phan tu tap test:", len(X_test))
print("Cac gia tri nhan khac nhau cua tap test:", np.unique(y_test))
print("-----------------------------")
print()


# Xay dung mo hinh KNN voi 7 lang gieng - Cau d
model_training = KNeighborsClassifier(
    n_neighbors=7,
    p=2
)

model_training.fit(X_train, y_train)


# Ket qua du doan
y_pred = model_training.predict(X_test)


# Danh gia do chinh xac toan bo tap test
accuracy_all = accuracy_score(y_test, y_pred)

print("DO CHINH XAC TOAN BO TAP TEST:")
print("Accuracy:", accuracy_all)
print()


# In 8 phan tu dau tien
print("8 PHAN TU DAU TIEN TRONG TAP TEST")

print("Nhan du doan:")
print(y_pred.tolist()[0:8])
print()

print("Nhan thuc te:")
print(y_test.tolist()[0:8])
print()


# Do chinh xac cua 8 phan tu dau tien
accuracy_8 = accuracy_score(
    y_test.iloc[0:8],
    y_pred[0:8]
)

print("Do chinh xac cua 8 phan tu dau tien:", accuracy_8)
print("-----------------------------")
print()


# Ma tran phan lop cua TOAN BO tap test
cm = confusion_matrix(
    y_test,
    y_pred,
    labels=labels
)

print("MA TRAN PHAN LOP CUA TOAN BO TAP TEST:")
print(cm)
print()


# Do chinh xac cua tung lop
accuracies = calculate_per_class(cm)

print("DO CHINH XAC CUA TUNG LOP:")

for i in range(len(accuracies)):
    print(
        "Lop %d: %.2f"
        % (labels[i], accuracies[i])
    )

print("-----------------------------")


# Ve ma tran phan lop
cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels
)

plt.figure(figsize=(8, 7))

sns.heatmap(
    cm_df,
    annot=True,
    fmt="d"
)

plt.title("Confusion matrix")
plt.xlabel("Predicted labels")
plt.ylabel("Actual labels")

plt.show()