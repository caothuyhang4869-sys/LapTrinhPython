n = input("Nhập n: ")

tong = 0

for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):

        so_con = n[i:j]
        so_con = int(so_con)

        tong = tong + so_con ** 2

print("Tổng S =", tong)