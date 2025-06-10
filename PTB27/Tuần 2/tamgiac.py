import math 

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"Diện tích của tam giác là: {s}")