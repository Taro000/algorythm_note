n = int(input())
nl = []

val_2 = [1, 2, 4, 8, 16, 32, 64]
for i in val_2:
    if i <= n: 
        nl.append(i)

print(max(nl))