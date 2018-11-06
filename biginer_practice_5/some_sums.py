N, A, B = map(int, input().split(" "))

n_num_list = []
for n in range(1, N+1):
    decimal_sum = 0
    for s in str(n):
        decimal_sum += int(s)
    if A <= decimal_sum <= B:
        n_num_list.append(n)

print(sum(n_num_list))