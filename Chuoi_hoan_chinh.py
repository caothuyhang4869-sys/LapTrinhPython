s = '''     Quê  hương
Quê  hương là   chùm khế   ngọt .
    Cho con trèo hái   mỗi ngày   .
Quê  hương là   đường  đi học .
  Con về  rợp bướm  vàng bay .
  Đỗ     Trung Quân    '''
  
tachdong = s.split('\n')
ketqua = []

for tach in tachdong :
    tach = tach.strip()   #xóa khoảng trắng đầu cuối
    tachtu = tach.split()   #tách từ bỏ khoảng trắng dư
    tach = " ".join(tachtu) #ghép từ lại có 1 khoảng trắng
    
    tach = tach.replace(" .",".")   #xóa khoảng trắng trước .
    tach = tach.replace(" ,",",")   #xóa khoảng trắng trước ,
    
    ketqua.append(tach)     #lưu từng dòng đã sửa
    
s = "\n".join(ketqua)       #ghép lại
print(s)
    