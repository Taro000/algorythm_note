s = '1.23, 2.4, 3.123'
total = 0

s_split = s.split(',')
for c in s_split:
    total += float(c)

print(total)