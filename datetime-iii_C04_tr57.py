from datetime import datetime

s = input("Nhập chuỗi ngày: ")

dt = datetime.strptime(s, "%b %d %Y %I:%M%p")

print(dt)