'''
Câu 4 Hãy viết chương trình kiểm tra một số nhập vào có phải là số hoàn hảo không
bằng Python. Biết rằng, N là một số hoàn hảo nếu như tổng các ước từ 1
-> (N - 1)
sẽ bằng N.
'''

n = int(input("Nhập số nguyên n: "))
tong=0
for i in range (1, n):
    if n%i==0:
        tong += i
if tong == n:
    print(n, "n là số hoàn hảo")
else:
    print(n, "không phải là số haonf hảo")
