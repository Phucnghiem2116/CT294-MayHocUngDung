'''
Câu 7. Giả sử chúng ta tạo ra một từ điển có tên là mydict, với mydict là các phần
tử mà có key là i và values của key là i∗i. Hãy viết chương trình nhập vào một số
nguyên N in ra từ điển có dạng trên. 
Ví dụ:
N = 5
mydict ={1: 1, 2: 4, 3: 9: 4: 16, 5: 25}
'''
n = int(input("Nhập vào một số nguyên N: "))
mydict = {}

for i in range(1, n + 1):
    mydict[i] = i * i

print("mydict =", mydict)