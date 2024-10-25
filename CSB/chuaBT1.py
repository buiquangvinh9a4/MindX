"""
# Bài 2
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
phone = int(input("Enter your phone number: "))

# \n        \t
print("Your registered name is\t", fname, lname, end = "====")
print("Your phone number is", phone)
"""


# Bài 3
a = 10
b = 3
#  in ra: 2 + 3 = 5
print("2 + 3 = ", a + b)
print(a,"+",b,"=",a+b)

# cú pháp f-string
print(f"{a} + {b} = {a + b}")