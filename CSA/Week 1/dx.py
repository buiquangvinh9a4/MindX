


n = int(input('Enter number: '))
p = 0
N = n
while N > 0:
    tmp = N % 10
    p = p * 10 + tmp
    N = N // 10
    
if p == n:
    print('YES')
else:
    print('NO')  
    
