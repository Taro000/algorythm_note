N, X = map(int, input().split(" "))
gram_list = []
for n in range(N):
    gram_list.append(int(input()))

dnt_cnt = 0
for i in gram_list:
    X = X - i
    dnt_cnt += 1

while X >= min(gram_list):
    X = X - min(gram_list)
    dnt_cnt += 1

print(dnt_cnt)
