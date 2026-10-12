#Câu 2. Viết chương trình nhập vào một ma trận MxN từ người dùng, sau đó tính
#tổng các phần tử của hàng được chỉ định. 
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

tonghang= int(input("Nhập vào hàng cần tính tông : "))
kq = sum(a[tonghang-1])

print("Tổng phần tử hàng", tonghang, "=", kq)