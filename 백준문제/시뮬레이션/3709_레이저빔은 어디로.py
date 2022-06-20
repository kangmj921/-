from collections import deque


def check_razer_direction(rx, ry):
    for i in range(4):
        nrx = rx + dx[i]
        nry = ry + dy[i]
        if 0 <= nrx <= n + 1 and 0 <= nry <= n + 1:
            continue
        if not i:
            i = 1
        elif i == 1:
            i = 0
        elif i == 2:
            i = 3
        else:
            i = 2
        return i


def change_razer_direction(r_d):
    if not r_d:
        return 3
    if r_d == 1:
        return 2
    if r_d == 2:
        return 0
    if r_d == 3:
        return 1


# 0 : 위쪽, 1 : 아래쪽, 2 : 왼쪽, 3 : 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for TC in range(int(input())):
    answer = (0, 0)
    n, r = map(int, input().split())
    board_list = [[0] * (n + 2) for _ in range(n + 2)]
    visit = [[-1] * (n + 2) for _ in range(n + 2)]
    for _ in range(r):
        x, y = map(int, input().split())
        board_list[x][y] = 'M'
    a, b = map(int, input().split())
    razer_direction = check_razer_direction(a, b)
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        # print(x, y)
        nx = x + dx[razer_direction]
        ny = y + dy[razer_direction]
        if ny < 0 or nx < 0 or ny > n + 1 or nx > n + 1:
            answer = (x, y)
            break
        if board_list[nx][ny] == 'M' and visit[ny][nx] != razer_direction:
            visit[ny][nx] = razer_direction
            razer_direction = change_razer_direction(razer_direction)
            queue.append((nx, ny))
        if not board_list[nx][ny]:
            queue.append((nx, ny))
    print(*answer)
