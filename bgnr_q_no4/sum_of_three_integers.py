K, S = map(int, input().split(" "))

S_cnt = 0
for x in range(K+1):
    for y in range(K+1):
        for z in range(K+1):
            if x + y + z == S:
                S_cnt += 1

print(S_cnt)
