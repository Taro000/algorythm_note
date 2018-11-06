N = int(input())


def sum_some(N):
    decimal_sum = 0
    while N > 0:
        decimal_sum += (N % 10)
        N //= 10
    return decimal_sum


result_func = sum_some(N)
if N % result_func == 0:
    print('Yes')
else:
    print('No')
