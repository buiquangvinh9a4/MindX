def UCLN(a, b):
    if b == 0:
        return a
    return UCLN(b, a % b)

def rutgon(a, b):
    if a == 0:
        return a, b
    else:
        return int(a / UCLN(a,b)), int(b/ UCLN(a, b))

A = int(input())
B = int(input())
C = int(input())

lst = [A, B, A, C, B, A, B, C, C, A, C, B]
lst_value = [A/B, A/C, B/A, B/C, C/A, C/B]
min_value = min(lst_value)
index_min = lst_value.index(min_value)
tu = lst[index_min * 2]
mau = lst[index_min * 2 + 1]

tu, mau = rutgon(tu,mau)
print(tu + mau)
