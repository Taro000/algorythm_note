N, L = map(int, input().split(' '))
str_list = [input() for i in range(N)]

str_list.sort()

bonded_str = ''

for j in str_list:
    bonded_str += j

print(bonded_str)