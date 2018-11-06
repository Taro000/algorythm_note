# 正攻法はこっちの方法らしい。AtCoderで紹介されてた。
N, A, B = map(int, input().split(" "))


def sum_decimal(n):
    answer_sum = 0
    while n > 0:
        answer_sum += n % 10
        n //= 10
    return answer_sum


total_num = 0

for n in range(1, N + 1):
    result_func = sum_decimal(n)
    if A <= result_func <= B:
        total_num += n

print(total_num)
