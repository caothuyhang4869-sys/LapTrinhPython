n = int(input("Nhập số nguyên dương n: "))

temp = n 
la_so_may_man = True

while n > 0:
    d = n % 10
    if d != 6 and d != 8:
        la_so_may_man = False
        break
    n //= 10

if la_so_may_man:
    print(temp, "là số may mắn")
else:
    print(temp, "KHÔNG phải số may mắn")