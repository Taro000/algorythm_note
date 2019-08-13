N, K = map(int, input().split(' '))
bars = [int(length) for length in input().split(' ')]
bars.sort(reverse=True)

sum_len = 0

for i in range(K):
    sum_len += bars[i]

print(sum_len)