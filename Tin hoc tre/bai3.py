def bai3(N, M):
    lst = [ ]
    for i in range(1, M + 1):
        if i % 2 == 1:
            lst.append(i)
        else:
            lst.append(N - i + 1)

    print(len(lst))
    return sum(lst[:M])

N = int(input())
M = int(input())
print(bai3(N, M))
