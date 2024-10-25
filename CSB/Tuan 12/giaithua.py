def numberOfFibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    lst = [1, 1]
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[n - 1]

def numberOfFibo2(n):
    if n <= 2:
        return 1
    return numberOfFibo2(n - 1) + numberOfFibo2(n - 2)


# Import time module
import time


start_time = time.time()

# Your code


end_time = time.time()
elapsed_time = end_time - start_time
print(f"- Thời gian chạy: {elapsed_time:.10f} giây")

