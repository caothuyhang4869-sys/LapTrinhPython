# iii. In ra các số từ 0 đến 9 không xuất hiện trong số điện thoại

S = input("Nhập số điện thoại: ")

tap_so = set(S)
print("Trong số điện thoại ",S," không chứa các số: ",end=" ")
for i in range(10):
    if str(i) not in tap_so:
        print(i, end=" ")