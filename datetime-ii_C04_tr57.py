from datetime import date

# nhập ngày 1
d1 = int(input("Ngày 1: "))
m1 = int(input("Tháng 1: "))
y1 = int(input("Năm 1: "))

# nhập ngày 2
d2 = int(input("Ngày 2: "))
m2 = int(input("Tháng 2: "))
y2 = int(input("Năm 2: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

kq = abs((date2 - date1).days)

print("Số ngày cách nhau:", kq) 