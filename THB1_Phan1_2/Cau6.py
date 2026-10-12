#Câu 6. Viết chương trình nhập vào hai ma trận cùng cấp. Tính tích của hai ma trậnđó.
# Câu 6. Nhập vào hai ma trận cùng cấp.
# Tính tích của hai ma trận đó.

m = int(input("Nhập vào số hàng m: "))
n = int(input("Nhập vào số cột n: "))

a = []
print("Nhập ma trận A:")
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        hang.append(x)
    a.append(hang)

b = []
print("Nhập ma trận B:")
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"Nhập phần tử B[{i}][{j}]: "))
        hang.append(x)
    b.append(hang)

print("Ma trận A:")
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()


print("Ma trận B:")
for i in range(m):
    for j in range(n):
        print(b[i][j], end=" ")
    print()
    
c = []
for i in range(m):
    hang = []
    for j in range(n):
        tong = 0
        for k in range(n):
            tong += a[i][k] * b[k][j]
        hang.append(tong)
    c.append(hang)

print("Ma trận tích A x B: ")
for i in range(m):
    for j in range(n):
        print(c[i][j], end=" ")
    print()