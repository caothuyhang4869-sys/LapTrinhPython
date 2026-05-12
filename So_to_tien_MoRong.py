a = int(input("Nhập số tiền hàng cần trả: "))
b = int(input("Nhập số tiền khách hàng đưa: "))

tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]

if a > b :
    print("Khách hàng còn thiếu ",a-b)
elif a == b:
    print("Cảm ơn khách hàng. Hẹn gặp lại!")

else:
    tien_thoi = b-a
    print("Số tiền cần thối lại là ",tien_thoi)
    print("Số tờ mỗi loại : ")
    
    tong_to = 0
    for loai in tien:
        so_to = tien_thoi // loai
        tien_thoi = tien_thoi % loai
        if so_to != 0:
            print("Loại ",loai," gồm ",so_to)
        tong_to = tong_to + so_to
    print("Tổng số tờ  là ",tong_to)
    input(".")
    print("Cảm ơn khách hàng. Hẹn gặp lại!")
    
    