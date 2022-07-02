import sys
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


# 1초 동안 아래 적힌 일이 순서대로 일어난다.
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
def dust_diffusion(a):
    temp_list = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A_list[i][j] > 0:
                temp = 0
                for k in range(4):
                    ni = i + dr[k]
                    nj = j + dc[k]
                    if 0 <= nj < C and 0 <= ni < R and A_list[ni][nj] != -1:
                        temp_list[ni][nj] += A_list[i][j] // 5
                        temp += 1
                temp_list[i][j] += A_list[i][j] - (A_list[i][j] // 5 * temp)
    for y, x in a:
        temp_list[y][x] = -1
    return temp_list


# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 공기 청정기의 바람에 의해 오른쪽으로 이동할 조건 = 공기 청정기와 같은 행에 위치하고 있음
# 위쪽, 아래쪽으로 이동하는 조건 = 열의 번호가 1이거나 N임. 이때 위 아래를 결정하는 것은 위쪽, 아래쪽
# 공기청정기의 바람인지가 결정함.
# 왼쪽으로 이동하는 조건 = 행이 1이거나 N임.
def dust_moved_by_air(a):
    dx = [[1, 0, -1, 0], [1, 0, -1, 0]]
    dy = [[0, -1, 0, 1], [0, 1, 0, -1]]
    for i in range(len(a)):
        y, x = a[i][0], a[i][1]
        direct = 0
        before = 0
        while True:
            ny = y + dy[i][direct]
            nx = x + dx[i][direct]
            if ny == a[not i][0] and nx == a[not i][1]:
                break
            if nx < 0 or ny < 0 or ny >= R or nx >= C:
                direct += 1
                continue
            if A_list[y][x] == -1:
                before = 0
            else:
                A_list[y][x], before = before, A_list[y][x]
            y = ny
            x = nx


# R이 행, C가 열 번호를 의미함.
R, C, T = map(int, input().split())
# 방의 크기는 최대 50 * 50, 구해야할 T초 후는 최대 1000초 후.
A_list = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
time = 0
air_conditioner = []
answer = 0
for i in range(R):
    for j in range(C):
        if A_list[i][j] == -1:
            air_conditioner.append((i, j))
for _ in range(T):
    A_list = dust_diffusion(air_conditioner)
    dust_moved_by_air(air_conditioner)
for i in range(R):
    for j in range(C):
        if A_list[i][j] > 0:
            answer += A_list[i][j]
print(answer)
