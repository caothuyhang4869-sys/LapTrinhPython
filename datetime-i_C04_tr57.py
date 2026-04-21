from datetime import datetime

now =  datetime.now()

print("Năm hiện tại: ",now.year)
print("Tháng hiện tại bằng chữ:", now.strftime("%B"))   # tháng bằng chữ
print("Tuần hiện tại là tuần thứ mấy trong năm:", now.strftime("%U"))
print("Tuần hiện tại là tuần thứ mấy trong tháng:", (now.day - 1)//7 + 1)       #tuần = (ngày - 1) // 7 + 1
print("Ngày hiện tại là ngày thứ mấy trong năm:", now.strftime("%j"))
print("Ngày dương lịch hiện tại là ngày:", now.day)
print("Thứ của ngày hiện tại:", now.strftime("%A"))
print("Giờ phút giây hiện tại:", now.strftime("%H:%M:%S"))

