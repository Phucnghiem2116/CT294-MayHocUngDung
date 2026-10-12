#Câu 5. Cho ma trận MxN được nhập vào từ người dùng,
#  sau đó hoán đổi 2 cột được chỉ định.
m= int(input("Nhập vào số hàng m"))
n= int(input("Nhập vào số cột n"))
a=[]
for i in range(m):
    hang=[]
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]: "))
        hang.append(x)
    a.append(hang)

print("Ma trận: ")
for i in range(m):
    for j in range(n):
        print(a[i][j], end= " ")
    print()

cot1= int(input("Nhập cột 1 hoán đổi"))
cot2= int(input("Nhập cột 2 hoán đổi"))

for i in range(m):
    r= a[i][cot1 - 1]
    a[i][cot1 - 1] = a[i][cot2 - 1]
    a[i][cot2 - 1] = r

print("Ma trận sau hoán đổi ")
for i in range(m):
    for j in range(n):
        print(a[i][j], end= " ")
    print()
