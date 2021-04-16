import sys
from itertools import combinations


# 풀이 시간 초과...
N, M = map(int, sys.stdin.readline().split())
city_info, house_info, chicken_store_info = [], [], []
for i in range(N):
    city_info.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    for j in range(N):
        if city_info[i][j] == 1:
            house_info.append([j, i])
        elif city_info[i][j] == 2:
            chicken_store_info.append([j, i])
selected_store = list(combinations(chicken_store_info, M))


def check_profit(a):
    result = 0
    sum_result = []
    for hx, hy in house_info:
        temp = 1e9
        for cx, cy in a:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result


result = 1e9
for c in selected_store:
    result = min(result, check_profit(c))
print(result)
