# 기울일때마다 구슬은 벽을 만날때까지 같은 방향으로 계속 간다.
# 각 구슬은 동시에 움직이므로, 빨간 구슬을 다 이동시킨 후, 파란 구슬도 같은 방향으로 이동시키면 편하겠지만
# 구슬이 서로 겹쳐있는 경우 문제가 된다.
# 구슬이 이동하는 방향에 다른 구슬을 만날경우, 벽 끝에 두개의 구슬을 놓고, 현재 이동 시키던 구슬을 뒤쪽에
# 놓는다.
# 이 모든 과정이 1번 기울여서 구슬을 움직인것이다.
# 만약 과정 중, 파란 구슬이 구멍으로 빠져나온다면, 횟수를 기록하지 않으며
# 빨간 구슬만 나왔을때 기록한다. 만약 이 기록이 10번보다 많다면 -1을 출력한다.
# 두 구슬이 동시에 움직여야 하므로, 두 구슬의 좌표를 모두 이용해서 BFS 해야 한다.
# 두 구슬의 좌표가 방문한 곳을 알기 위해, N * M * N * M 배열로
# ry rx by bx 를 모두 기록할 수 있는 배열로 해야한다.
import sys
import math
from collections import deque


def move(y, x, dy, dx):
    cnt = 0
    while board_list[y + dy][x + dx] != '#' and board_list[y][x] != 'O':
        x += dx
        y += dy
        cnt += 1
    return y, x, cnt


def BFS(q):
    global answer
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        # print(y, x, cnt, color, 'dasdafs')
        if cnt > 10:
            break
        for i in range(4):
            nry, nrx, r_cnt = move(ry, rx, dy[i], dx[i])
            nby, nbx, b_cnt = move(by, bx, dy[i], dx[i])
            if board_list[nby][nbx] != 'O':
                if board_list[nry][nrx] == 'O':
                    answer = min(answer, cnt)
                if nrx == nbx and nry == nby:
                    if r_cnt > b_cnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visit[nry][nrx][nby][nbx]:
                    visit[nry][nrx][nby][nbx] = True
                    queue.append((nrx, nry, nbx, nby, cnt + 1))


answer = math.inf
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N, M = map(int, input().split())
board_list = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
queue = deque()
for i in range(N):
    for j in range(M):
        if board_list[i][j] == 'B':
            bx, by = j, i
        if board_list[i][j] == 'R':
            rx, ry = j, i
queue.append((rx, ry, bx, by, 1))
visit[ry][rx][by][bx] = True
BFS(queue)
if answer == math.inf:
    answer = -1
print(answer)
