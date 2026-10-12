#Câu 4. Viết chương trình tạo ra ma trận 4x4 với các giá trị cách nhau 2 đơn vị. 
# In ra ma trận và tính tổng hàng thứ 2 của ma trận đó. 
a=[]
n=1
for i in range(4):
    hang=[]
    for j in range(4):
        hang.append(n)
        n=n+2
    a.append(hang)

print("Ma trận")
for i in range(4):
    for j in range(4):
        print(a[i][j], end=" ")
    print()
kq= sum(a[1])
print("Tổng hàng thứ 2 =", kq)