from math import sqrt

N = int(input())

point_list = []
for n in range(N):
    x, y = map(int, input().split(" "))
    point_list.append((x, y))

distance_list = []
for p in point_list:
    for other_p in point_list:
        distance_list.append(sqrt((p[0]-other_p[0]) ** 2 + (p[1] - other_p[1]) ** 2))

print(max(distance_list))
