#Câu 9. Cho một từ điển, với các phần tử có key là i và values của key là i2Viết 
#chương trình nhập vào số nguyên N in ra từ điển trên

n = int(input("Nhập vào số nguyên n: "))
a={}
for i in range(1, n+1):
    a[i] = i*i
print(a)