n = int(input("Nhập số nguyên dương n: "))

tong = 0
tich = 1

while n > 0:
        t = n % 10
        tong += t
        tich *= t
        n //= 10
    
print("Tổng = ",tong)
print("Tích =  ",tich)

max = 0
while n > 0:
    d = n % 10
    if d > max :
        max = d 
    n//=10
    
print("Số lớn nhất là : ",max)