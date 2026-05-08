# ĐỌC FILE
with open("test.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()

# TÁCH TỪ
ds_tu = noi_dung.split()

# TẠO TỪ ĐIỂN VÀ DANH SÁCH VỊ TRÍ
tu_dien = []
vi_tri = []

for tu in ds_tu:

    if tu not in tu_dien:
        tu_dien.append(tu)

    vi_tri.append(tu_dien.index(tu))

# GHI FILE NÉN
with open("nen.txt", "w", encoding="utf-8") as f:

    f.write(" ".join(tu_dien))
    f.write("\n")

    for x in vi_tri:
        f.write(str(x) + " ")

print("Đã nén file!")

# ĐỌC FILE NÉN
with open("nen.txt", "r", encoding="utf-8") as f:

    dong1 = f.readline().strip()
    dong2 = f.readline().strip()

# KHÔI PHỤC
tu_dien = dong1.split()
vi_tri = dong2.split()

van_ban = ""

for x in vi_tri:
    van_ban += tu_dien[int(x)] + " "

print("\nVăn bản phục hồi:")
print(van_ban)