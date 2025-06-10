s = int(input("Nhập số giây: "))

h = s // 3600
p = s % 3600 // 60
s = s - (h * 3600 + p * 60)
print("Giờ: ", h)
print(p)
print(s)