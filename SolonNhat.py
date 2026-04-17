n = int(input("Nhập số nguyên dương n: "))

max = 0
while n > 0:
    d = n % 10
    if d > max :
        max = d 
    n//=10
    
print("Số lớn nhất là : ",max)