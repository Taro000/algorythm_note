N, x = map(int, input().split(' '))
candy_num = list(map(int, input().split(' ')))

candy_num.sort()

sum_want = 0
num_child = 0

for i in range(N):
    sum_want += candy_num[i]
    if i == N-1 and sum_want < x:
        break
    if sum_want > x:
        break
    else:
        num_child += 1

print(num_child)