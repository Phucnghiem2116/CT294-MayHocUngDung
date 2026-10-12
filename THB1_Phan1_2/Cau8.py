#Câu 8. Cho một từ điển có 10 phần tử ngẫu nhiên từ 1 tới 10. Viết chương trình
#chuyển từ điển đó thành một mảng 2 chiều
import random
a={}
for i in range(1, 11):
    a[i] = random.randint(1,10)
print(a)
mang=[]
for n,m in a.items():
    mang.append([n, m])
print("Mange 2 chiều: ")
for i in range(len(mang)):
    print(mang[i]) 
