#Câu 3. Viết chương trình tạo một ma trận 5x5 với các giá trị từ 1 đến 25. In ra ma
#trận và tính tổng các phần tử của cột được chỉ định.
a=[]
n=1
for i in range(5):
    hang=[]
    for j in range(5):
        hang.append(n)
        n=n+1
    a.append(hang)

print("Ma trận")
for i in range(5):
    for j in range(5):
        print(a[i][j], end=" ")
    print()
b= int(input("Nhập vào cot cần tính tổng: "))
kq=0
for i in range(5):
    kq= kq+ a[i][b-1]
print("Tổng các phần tử cột", b, "=",kq)