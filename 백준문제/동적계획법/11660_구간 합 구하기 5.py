# 구간의 누적합을 구해야한다.

import sys


N, M = map(int, input().split())
chart = [list(map(int, input().split())) for _ in range(N)]
dp_list = [[0] * N for _ in range(N)]
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        print(chart[x1 - 1][y1 - 1])
    else:
        pass
