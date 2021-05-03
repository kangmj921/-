import sys

point_list = []
for _ in range(int(input())):
    point_list.append(list(map(int, sys.stdin.readline().split())))
point_list.sort(key=lambda x : (x[1], x[0]))
for x, y in point_list:
    print(x, y)
