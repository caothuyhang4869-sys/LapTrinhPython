def tong_chu_so(n):
    # B1: điều kiện dừng
    if n == 0:
        return 0

    # B2: gọi đệ quy
    return n % 10 + tong_chu_so(n // 10)

n = int(input("Nhập n: "))
print("Tổng chữ số =", tong_chu_so(n))