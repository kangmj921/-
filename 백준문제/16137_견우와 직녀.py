from collections import deque
import sys


def check(y, x):
    r, c = 0, 0
    if 0 <= y - 1 and not map_inf[y - 1][x]:
        r = 1
    elif y + 1 < N and not map_inf[y + 1][x]:
        r = 1
    if x + 1 < N and not map_inf[y][x + 1]:
        c = 1
    elif 0 <= x - 1 and not map_inf[y][x - 1]:
        c = 1
    if r and c:
        return True
    return False


def BFS():
    global answer
    queue = deque()
    queue.append((0, 0, 0))
    v = [[0] * N for _ in range(N)]
    v[0][0] = 1
    while queue:
        y, x, cnt = queue.popleft()
        if cnt >= answer:
            break
        if y == N - 1 and x == N - 1:
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if map_inf[ny][nx] == 1:
                if not v[ny][nx]:
                    v[ny][nx] = 1
                    queue.append((ny, nx, cnt + 1))
            elif map_inf[ny][nx] > 1:
                if map_inf[y][x] > 1:
                    continue
                if not v[ny][nx]:
                    if not (cnt + 1) % map_inf[ny][nx]:
                        queue.append((ny, nx, cnt + 1))
                    else:
                        queue.append((y, x, cnt + 1))
    return 10 ** 10


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 10 ** 10
N, M = map(int, input().split())
map_inf = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not map_inf[i][j]:
            if check(i, j):
                continue
            map_inf[i][j] = M
            result = BFS()
            map_inf[i][j] = 0
            if result < answer:
                answer = result
print(answer)
