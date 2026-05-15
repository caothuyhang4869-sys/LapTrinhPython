a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

dem = 0

print("Các số thân thiện là:")

for i in range(a, b + 1):
    dao = str(i)[::-1]
    dao = int(dao)
    # Tìm UCLN
    x = i
    y = dao
    while y != 0:
        x, y = y, x % y

    # Nếu UCLN = 1
    if x == 1:
        print(i, end=" ")
        dem += 1

print("\nSố lượng:", dem)