A = int(input())
B = int(input())
C = int(input())
X = int(input())

x_cnt = 0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if a * 500 + b * 100 + c * 50 == X:
                x_cnt += 1

print(x_cnt)
