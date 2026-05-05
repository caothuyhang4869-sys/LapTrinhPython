from collections import Counter

# Nhập 2 chuỗi
S1 = input("Nhập chuỗi S1: ")
S2 = input("Nhập chuỗi S2: ")

# Đưa vào dictionary Counter
dict1 = Counter(S1)
dict2 = Counter(S2)

# a) Ký tự xuất hiện trong cả 2 chuỗi
print("\nCác ký tự xuất hiện trong cả 2 chuỗi:", end=" ")

for i in dict1:
    if i in dict2:
        print(i, end=" ")

# b) Đếm ký tự khác nhau
dem1 = 0
dem2 = 0

for i in dict1:
    if i not in dict2:
        dem1 += 1

for i in dict2:
    if i not in dict1:
        dem2 += 1

print("\n\nSố ký tự có trong S1 nhưng không có trong S2 =", dem1)
print("Số ký tự có trong S2 nhưng không có trong S1 =", dem2)

# c) In ký tự khác nhau
print("\nKý tự có trong S1 nhưng không có trong S2:", end=" ")

for i in dict1:
    if i not in dict2:
        print(i, end=" ")

print("\nKý tự có trong S2 nhưng không có trong S1:", end=" ")

for i in dict2:
    if i not in dict1:
        print(i, end=" ")