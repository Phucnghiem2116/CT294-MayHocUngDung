import numpy as np

import pandas as pd

from sklearn.preprocessing import MinMaxScaler

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

            accuracy = correct_prediction / total_prediction

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
df = pd.read_csv("winequality-red.csv", sep=";")


# Kich thuoc du lieu
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


# In du lieu cac thuoc tinh
print_data(X_data)


# =========================================================
# CAU C: CHIA DU LIEU THANH 4 PHAN TRAIN VA 1 PHAN TEST
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X_data,
    y_data,
    test_size=0.2,
    random_state=42
)


# =========================================================
# CHUAN HOA DU LIEU
# =========================================================

scaler = MinMaxScaler()

# Chi fit tren tap train
X_train_scaler = scaler.fit_transform(X_train)

# Ap dung scaler da fit cho tap test
X_test_scaler = scaler.transform(X_test)


# Tao DataFrame de xem du lieu sau khi chuan hoa
df_Scaler = pd.DataFrame(
    X_train_scaler,
    columns=X_data.columns
)


print("Du lieu truoc khi chuan hoa:")

print(X_train.head())

print()


print("Du lieu sau khi chuan hoa:")

print(df_Scaler.head())

print()


# =========================================================
# THONG TIN TAP TEST - CAU C
# =========================================================

print("THONG TIN TAP TEST")

print("So luong phan tu tap test:", len(X_test))

print(
    "Cac gia tri nhan khac nhau cua tap test:",
    np.unique(y_test)
)

print("-----------------------------")

print()


# =========================================================
# CAU D: XAY DUNG MO HINH KNN VOI 9 LANG GIENG
# =========================================================

model_training = KNeighborsClassifier(
    n_neighbors=9,
    p=2
)


# Huan luyen mo hinh
model_training.fit(X_train_scaler, y_train)


# Du doan tap test
y_pred = model_training.predict(X_test_scaler)


# =========================================================
# 1. DO CHINH XAC TOAN BO TAP TEST
# =========================================================

accuracy_all = accuracy_score(y_test, y_pred)

print("DO CHINH XAC TOAN BO TAP TEST:")

print("Accuracy:", accuracy_all)

print()



# IN 7 PHAN TU DAU TIEN


print("7 PHAN TU DAU TIEN TRONG TAP TEST")

print("Nhan du doan:")

print(y_pred.tolist()[0:7])

print()


print("Nhan thuc te:")

print(y_test.tolist()[0:7])

print()


# Tinh accuracy cua 7 phan tu dau tien
accuracy_7 = accuracy_score(
    y_test.iloc[0:7],
    y_pred[0:7]
)

print("Do chinh xac cua 7 phan tu dau tien:", accuracy_7)

print("-----------------------------")

print()



# MA TRAN PHAN LOP CUA TOAN BO TAP TEST


cm = confusion_matrix(
    y_test,
    y_pred,
    labels=labels
)


print("MA TRAN PHAN LOP CUA TOAN BO TAP TEST:")

print(cm)

print()


# DO CHINH XAC CUA TUNG LOP

accuracies = calculate_per_class(cm)

print("DO CHINH XAC CUA TUNG LOP:")

for i in range(len(accuracies)):

    print(
        "Lop %d: %.2f"
        % (labels[i], accuracies[i])
    )

print("-----------------------------")



# VE MA TRAN PHAN LOP


cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels
)


plt.figure(figsize=(7, 6))

sns.heatmap(
    cm_df,
    annot=True,
    fmt="d"
)

plt.title("Confusion matrix")

plt.xlabel("Predicted labels")

plt.ylabel("Actual labels")

plt.show()