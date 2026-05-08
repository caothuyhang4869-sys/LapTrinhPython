# iv. Cho nhập 1 chuỗi (S). Tìm từ đầu tiên lặp lại trong S

S = input("Nhập chuỗi: ")
cac_tu = S.split()
tap_hop = set()

for tu in cac_tu:
    if tu in tap_hop:
        print("Từ đầu tiên lặp lại là:", tu)
        break
    else:
        tap_hop.add(tu)
else:
    print("None")