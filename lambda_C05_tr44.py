import math

f_a = lambda n: abs(n)
f_b = lambda n: n + 15
f_c = lambda x, y: x * y
f_d = lambda n: (n % 13 == 0 or n % 19 == 0)
f_e = lambda r: math.pi * r * r
f_f = lambda d, r: 2 * (d + r)
f_g = lambda n: int(n**0.5)**2 == n


# kiểm tra số nguyên tố
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# dùng lambda gọi lại def
f_h = lambda n: isPrime(n)

# phân loại tam giác
def tamgiac(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Không phải tam giác"
    elif a == b == c:
        return "Tam giác đều"
    elif a == b or b == c or a == c:
        return "Tam giác cân"
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        return "Tam giác vuông"
    else:
        return "Tam giác thường"

f_i = lambda a, b, c: tamgiac(a, b, c)

n = int(input("Nhập số nguyên n: "))
print("a) |n| =", f_a(n))
print("b) n + 15 =", f_b(n))
print("d) Bội 13 hoặc 19:", f_d(n))
print("g) Số chính phương:", f_g(n))
print("h) Số nguyên tố:", f_h(n))

print("\nTích x, y?")
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
print("c) x * y =", f_c(x, y))

print("\nDiện tích hình tròn? ")
r = float(input("Nhập bán kính r: "))
print("e) Diện tích hình tròn =", f_e(r))

print("\nChu vi hình chữ nhật?")
d = float(input("Nhập chiều dài: "))
r2 = float(input("Nhập chiều rộng: "))
print("f) Chu vi hình chữ nhật =", f_f(d, r2))

print("\nKiểm tra tam giác? ")
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
print("i) Kết luận:", f_i(a, b, c))