'''
Câu 1. Viết chương trình nhập từ bàn phím danh sách a. Hãy tính giá trị trung bình
của các phần tử trong danh sách a và trả về kết quả giá trị trung bình. (Việc nhập chỉ
kết thúc nếu gặp ký tự “$”). 
'''
a=[] 
while True:
    b= input("Nhập vào phần tử số nguyên: ")
    if b=="$":
        break
    a.append(float(b))
tong=sum(a)
avg=tong/len(a)
print("Danh sach a: ", a)
print("Trung bình cộng: ", avg)