 lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst