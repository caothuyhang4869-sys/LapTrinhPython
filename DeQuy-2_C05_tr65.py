def GiaiThua(n):
    if n == 1 :
        return 1
    return GiaiThua(n-1) * n
    
n = int(input("Nhập n: "))
print(f"{n}! = {GiaiThua(n)}")