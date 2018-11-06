N = int(input())


def check_digit(j):
    digit_sum = 0
    while j > 0:
        digit_sum += j % 10
        j //= 10
    return digit_sum


ten_power_list = [10**x for x in range(6)]

if N in ten_power_list:
    ab_sum_min = 10
else:
    ab_sum_min = check_digit(N)


print(ab_sum_min)