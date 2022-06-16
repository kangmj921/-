# 대나무 숲의 크기가 최대 500 * 500이므로 리스트의 모든 요소를 돌면서
# 최대 4 * N * N이 걸릴 수 있는 탐색을 500 * 500번 구하고
# 최댓값을 구하면 시간 초과에 걸릴 수 밖에 없다.
# a에서 b로 갈 수 있으면 a가 곧 b보다 크다는 의미며,
# b에서 구한 경로 + 1임.
# 경로를 저장하는 리스트는 모두 -1로 초기화함.
# 즉, 0,0에서 시작하면서 경로의 수가 없는 것만 실행함.
# 14의 주위엔 9, 1즉 이동할 수 없는 것만 있으므로, 0을 경로 저장.
# 9의 주위에 14, 11, 12가 있음,
# 14 11 12 경로의 수 중 최대값 + 1
# 14 11 12에서 또 이동할 수 없는 거 가려내면,
# 11 밖에 안남는데, 11은 또 15의 경로의 수 + 1
# 즉, DP를 이용하여 다음 갈 수 있는 칸들이 가지고 있는 경로 중 최대 값을 구한다.
# 이때 재귀를 돌릴때, 이미 경로가 구해진 곳, 즉 DP에 저장된 값이 -1이 아닌 경우는
# 또 재귀를 돌릴 필요가 없으므로, 백트래킹도 해준다.
# 재귀 제한 계속 걸리면 그냥 10억으로 박아야겠다.

import sys
sys.setrecursionlimit(10**9)


def search(y, x):
    temp = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if bamboo_list[ny][nx] > bamboo_list[y][x]:
            if dp_list[ny][nx] == -1:
                dp_list[ny][nx] = search(ny, nx)
            temp = max(temp, dp_list[ny][nx] + 1)
    if temp:
        return temp
    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
dp_list = [[-1] * n for _ in range(n)]
bamboo_list = []
# bamboo_list = [[i for i in range(1, 501)] for _ in range(500)]
# print(bamboo_list, len(bamboo_list), len(bamboo_list[0]))
answer = 0
for _ in range(n):
    bamboo_list.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if dp_list[i][j] == -1:
            dp_list[i][j] = search(i, j)
            answer = max(answer, dp_list[i][j])
print(answer + 1)
