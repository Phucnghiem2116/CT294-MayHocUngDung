'''
Câu 3 Tam giác Floyd là một tam giác vuông được tạo từ các số tự nhiên. Các số
trong tam giác Floyd có giá trị tăng dần. 
Dưới đây là hình minh họa cho tam giác Floyd đơn giản gồm các số từ 1 tới 10 (số
hàng là 4).
1
2 3
4 5 6
7 8 9 10
'''
n= int(input('Vui lòng nhập vào số nguyên n: '))
a=1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(a, end=" ")
        a=a+1
    print()

