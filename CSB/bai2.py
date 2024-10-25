s = "Lương Bá Dũng"
print("Tên: ", s)
print(f"Độ dài của {s} là: {len(s)}")

# cắt 1 kí tự
print(s[6])

# cắt nhiều kí tự - cắt đoạn
#  s [start: end - 1: step]
print(s[0:5])


# ví dụ
s = "0123456789"
print(s[0: len(s): 3]) 
# in ngược xâu
print(s[::-1])

# index l->r : 0 1 2 3 4 5 .... len(s) - 1
# index r->l : -1 -2 -3 -4 -5 ...... len(s) * (-1)


a = 1234 # 123

du1 = a % 10
a = a // 10  # 123

du2 = a % 10
a = a // 10   


"""
    Quy tắc đặt tên biến:
    - Không được đặt tên trùng với từ khóa của ngôn ngữ
    - Không chứa kí tự số ở đầu:  1bien, 1a, 2b -> bien1, a1, b2
    - Không chứa kí tự đặc biệt (ngoại trừ dấu _):
              bien)1, bien#2, bien 1
              -> bien_1 , bien_2,....
"""

# hàm sqrt trong thư viện math
"""
from math import sqrt

number = float(input())
print(number ** 0.5)
print(sqrt(number))
"""
s = "05/19/1890"
day = s[3:5]
month = s[:2]
year = s[6:]
print(f"Format Date: {day}/{month}/{year}")