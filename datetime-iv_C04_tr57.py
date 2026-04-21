from datetime import *

now = datetime.now()

new_time = now + timedelta(seconds=5)

print("Hiện tại:", now.strftime("%H:%M:%S"))
print("Thêm 5 giây:", new_time.strftime("%H:%M:%S"))