# 구슬 탈출 2와 비슷하지만, 이번엔 구슬을 빼낼때, 기울인 방향도 같이 출력해줘야 하는 문제이다.
from collections import deque
from copy import deepcopy

move_direction = {0: 'L', 1: 'R', 2: 'U', 3: 'D'}


def move(y, x, d):
    c = 0
    while board_list[y + dy[d]][x + dx[d]] != '#' and board_list[y][x] != 'O':
        y += dy[d]
        x += dx[d]
        c += 1
    return y, x, c


def bfs(by, bx, ry, rx):
    global answer
    queue = deque()
    queue.append((by, bx, ry, rx, []))
    visit[by][bx][ry][rx] = True
    while queue:
        check = ''
        by, bx, ry, rx, move_list = queue.popleft()
        if len(move_list) > 10:
            break
        for i in range(4):
            nby, nbx, b_cnt = move(by, bx, i)
            nry, nrx, r_cnt = move(ry, rx, i)
            if board_list[nby][nbx] != 'O':
                if board_list[nry][nrx] == 'O':
                    if len(move_list) < len(answer):
                        answer = deepcopy(move_list + [move_direction[i]])
                if nry == nby and nrx == nbx:
                    if r_cnt > b_cnt:  # R이 B보다 뒤에 있었음.
                        nry -= dy[i]
                        nrx -= dx[i]
                    else:
                        nby -= dy[i]
                        nbx -= dx[i]
                if not visit[nby][nbx][nry][nrx]:
                    visit[nby][nbx][nry][nrx] = True
                    queue.append((nby, nbx, nry, nrx, move_list + [move_direction[i]]))


answer = [0] * 11
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
board_list = [list(input().rstrip()) for _ in range(N)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board_list[i][j] == 'R':
            ry, rx = i, j
        elif board_list[i][j] == 'B':
            by, bx = i, j
bfs(by, bx, ry, rx)
if len(answer) > 10:
    print(-1)
else:
    print(len(answer))
    for a in answer:
        print(a, end='')
