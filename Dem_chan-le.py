n = int(input("Nhập số nguyên dương n: "))

chan = 0
le = 0

while n > 0:
    d = n % 10
    if d % 2 == 0 :
        chan += 1
    else:
        le += 1
    n//=10
    
print("Số lượng chẳn: ",chan)
print("Số lượng lẻ: ",le)
