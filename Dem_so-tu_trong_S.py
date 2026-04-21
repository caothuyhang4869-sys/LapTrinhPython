s = '''Chiều chiều trước bến Văn Lâu
        Ai ngồi, ai câu, ai sầu , ai thảm
        Ai thương, ai cảm, ai nhớ, ai trông
        Thuyền ai tháp thoáng ven sông
        Đưa câu mái vẩy chạnh lòng nước non '''

word = input("Nhập từ cần đếm: ")

print("Số từ", word, "là", s.count(word, 0, len(s)))

