"""
    n = 4
    *
    **
    ***
    ****

"""
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end = "")
    print("*" * i)
