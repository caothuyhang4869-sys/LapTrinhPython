tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

tong_to = 0

so_tien = int(input("Nhập số tiền : "))

for loai in tien :
    so_to = so_tien // loai
    so_tien = so_tien % loai
    print("Loai", loai, "gom", so_to, "to")

    tong_to = tong_to + so_to
    
print("Tổng cộng có ",tong_to," tờ.")