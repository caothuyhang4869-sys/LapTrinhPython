def Fibonaci(n):
    if n < 2 :
        return  1
    return Fibonaci(n-1) + Fibonaci(n-2)

n = int(input("Nhập n: "))
print(f"Số hạng thứ {n} của chuỗi Fibonaci là {Fibonaci(n)}")