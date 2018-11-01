num_num = int(input())
num_list = list(map(int, input().split(" ")))

diff_list = []
for i in num_list:
    for j in range(num_num):
        diff_list.append(i - num_list[j])

print(num_num)
print(max(diff_list))