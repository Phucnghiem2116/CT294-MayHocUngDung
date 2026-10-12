import pandas as pd
import numpy as np

df = pd.read_csv("iris_data.csv", sep=",", header=None)

#ten cot
df.columns = [
    "thuoc_tinh_" + str(i + 1) for i in range(4)
] + ["nhan"]

n = int(input("Nhap so dong dau tien muon hien thi: "))
print(df.head(n))


n = int(input("Nhap so dong cuoi cung muon hien thi: "))
print(df.tail(n))

print()

t = df.shape
print("So hang du lieu: " + str(t[0]))
print("So cot du lieu: " + str(t[1]))

print()
# du lieu cot nhan

y_data = df.loc[:, "nhan"]
labels = np.unique(y_data)
# tap cac nhan
print("Du lieu cua nhan: ")
print(labels)
print()


# ten cac thuoc tinh
x_data = df.iloc[:, 0:4]

print("Ten cac thuoc tinh: ")

print(x_data.columns)

print()


print("Du lieu cua cac thuoc tinh: ")
for i in range(0, 4, 1):
    x = x_data.iloc[:, i]
    print("Du lieu cua thuoc tinh thu %d: " % (i + 1))
    print(x)
    print()

print("Thong ke du lieu: ")

print(df.describe())