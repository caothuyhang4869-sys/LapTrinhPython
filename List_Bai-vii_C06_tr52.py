#C06 List
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

L = []

while True:
    x = int(input("Nhập số nguyên: "))
    L.append(x)

    tiep = input("Tiếp tục không? (Y/N): ")

    if tiep.upper() == 'N':
        break

print("\nDanh sách vừa nhập:", L)

# a) In các số nguyên tố trong L
print("\nCác số nguyên tố trong list: ",end =" ")


for i in L :
    if la_so_nguyen_to(i):
        print(i, end =" ")
        
# b) Trung bình cộng số âm và trung bình cộng số dương
tong_am = 0
dem_am = 0

tong_duong = 0
dem_duong = 0

for i in L :
    if i < 0 :
        dem_am += 1
        tong_am += i
    elif i > 0 :
        dem_duong += 1
        tong_duong += i

if dem_am > 0 :
    print("\n\nTrung bình cộng các số âm: ",tong_am / dem_am)
else:
    print("\n\nKhông có số âm trong List.")
    
if dem_duong > 0 :
    print("Trung bình cộng các số dương: ",tong_duong / dem_duong)
else:
    print("Không có số dương trong List.")
    
    
# c) Số lớn nhất và nhỏ nhất
print("\nSố lớn nhất =", max(L))
print("Số nhỏ nhất =", min(L))

# d) Kiểm tra tăng dần
tang_dan = lambda L: all(
    L[i] <= L[i + 1]
    for i in range(len(L) - 1)
)

if tang_dan(L):
    print("\nList đã được sắp xếp tăng dần")
else:
    print("\nList chưa được sắp xếp tăng dần")
    