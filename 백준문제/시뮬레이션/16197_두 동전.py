# 두 개의 동전이 보드에 있는데 버튼을 최소한으로 눌러 동전을 보드 밖으로 떨어뜨려야한다.
# 구슬탈출 문제와 비슷한 로직으로 풀었다.
from collections import deque


def check_coin_fall_num(y1, x1, y2, x2):
    if y1 < 0 or y2 < 0 or y1 >= N or y2 >= N:
        if y1 == y2:
            return False
    if x1 < 0 or x2 < 0 or x1 >= M or x2 >= M:
        if x1 == x2:
            return False
    return True


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board_list = [list(input().rstrip()) for _ in range(N)]
visit_list = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
time = 0
coin_list = []
for i in range(N):
    for j in range(M):
        if board_list[i][j] == 'o':
            coin_list += [i, j]
queue = deque()
queue.append(tuple((coin_list + [0])))
while queue:
    y_1, x_1, y_2, x_2, cnt = queue.popleft()
    visit_list[y_1][x_1][y_2][x_2] = True
    if cnt >= 10:
        break
    for i in range(4):
        ny_1, nx_1 = y_1 + dy[i], x_1 + dx[i]
        ny_2, nx_2 = y_2 + dy[i], x_2 + dx[i]
        if nx_1 < 0 or ny_2 < 0 or nx_2 < 0 or ny_1 < 0 or nx_1 >= M or ny_2 >= N or nx_2 >= M or ny_1 >= N:
            if check_coin_fall_num(ny_1, nx_1, ny_2, nx_2):
                print(cnt + 1)
                exit()
            continue
        if board_list[ny_1][nx_1] == '#' and board_list[ny_2][nx_2] == '#':
            continue
        if not visit_list[ny_1][nx_1][ny_2][nx_2]:
            if board_list[ny_1][nx_1] == '#':
                queue.append((y_1, x_1, ny_2, nx_2, cnt + 1))
            elif board_list[ny_2][nx_2] == '#':
                queue.append((ny_1, nx_1, y_2, x_2, cnt + 1))
            else:
                queue.append((ny_1, nx_1, ny_2, nx_2, cnt + 1))
print(-1)
