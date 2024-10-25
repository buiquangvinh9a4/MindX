import math

a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))
if a == 0:
    x = -c / b
    print(f'x = {x}')
else:
    delta =  b * b - 4 * a * c
    if delta  > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
    elif delta == 0:
        x = -b / (2 * a)
        print(f'x = {x}')
    else:
        print('Phương trình vô nghiệm')

