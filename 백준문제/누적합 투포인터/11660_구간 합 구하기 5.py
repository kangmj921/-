import sys


N, M = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(N)]
S_list = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        S_list[i][j] = S_list[i][j - 1] + S_list[i - 1][j] - S_list[i - 1][j - 1] + N_list[i - 1][j - 1]
# print(S_list)
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(S_list[x2][y2] - S_list[x1 - 1][y2] - S_list[x2][y1 - 1] + S_list[x1 - 1][y1 - 1])
