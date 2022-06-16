import math
from copy import deepcopy


dict_ = {1: [[0], [1], [2], [3]], 2: [[0, 1], [2, 3]],
         3: [[0, 2], [0, 3], [1, 2], [1, 3]], 4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
         5: [[0, 1, 2, 3]]}  # 각 cctv 가 비출 수 있는 방향의 경우를 dx, dy에 맞추어
# 모든 경우의 수 표현


def check_cctv_view(view_direction, cctv_y, cctv_x, a):
    for i in view_direction:
        ncy = cctv_y + dy[i]
        ncx = cctv_x + dx[i]
        while 0 <= ncy < N and 0 <= ncx < M and a[ncy][ncx] != 6:
            if a[ncy][ncx] == 0:
                a[ncy][ncx] = '#'
            ncy += dy[i]
            ncx += dx[i]
    return a


def search(index, of):
    global answer
    if index == len(cctv_list):
        result = 0
        for n in range(N):
            for m in range(M):
                if not of[n][m]:
                    result += 1
        # print(of, result)
        answer = min(answer, result)
        return
    cctv = cctv_list[index]
    for case in dict_[cctv[0]]:  # 해당 cctv 가 비추는 방향의 모든 경우의 수대로 비춰봄.
        a = deepcopy(of)
        new_of = check_cctv_view(case, cctv[1], cctv[2], a)
        search(index + 1, new_of)


dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())  # 최대 8 * 8 크기
answer = math.inf
office_list = [list(map(int, input().split())) for _ in range(N)]
cctv_list = []
for i in range(N):
    for j in range(M):
        if 1 <= office_list[i][j] <= 5:
            cctv_list.append((office_list[i][j], i, j))
search(0, office_list)
print(answer)
