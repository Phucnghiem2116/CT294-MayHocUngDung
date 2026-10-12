#Câu 2 Viết chương trình Python
# liệt kê tất cả các ước số của N với N được nhập vào từ bàn phím

n = int(input("Nhập số nguyên n: "))
for i in range (1, n+1):
    if n%i==0:
        print(i)
