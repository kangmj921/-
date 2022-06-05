import sys


def DFS(y, x, n, total, d):
    global answer
    if n == 4:
        answer = max(answer, total)
        return
    if n == 2:
        temp = 0
        if d == 0:
            if x - 1 >= 0:
                if y + 1 < N:
                    temp = paper_num[y][x - 1] + paper_num[y + 1][x]
                if y - 1 >= 0:
                    temp = max(temp, paper_num[y][x - 1] + paper_num[y - 1][x])
        elif d == 1:
            if x + 1 < M:
                if y + 1 < N:
                    temp = paper_num[y][x + 1] + paper_num[y + 1][x]
                if y - 1 >= 0:
                    temp = max(temp, paper_num[y][x + 1] + paper_num[y - 1][x])
        elif d == 3:
            if y + 1 < N:
                if x + 1 < M:
                    temp = paper_num[y + 1][x] + paper_num[y][x + 1]
                if x - 1 >= 0:
                    temp = max(temp, paper_num[y + 1][x] + paper_num[y][x - 1])
        elif d == 2:
            if y - 1 >= 0:
                if x + 1 < M:
                    temp = paper_num[y - 1][x] + paper_num[y][x + 1]
                if x - 1 >= 0:
                    temp = max(temp, paper_num[y - 1][x] + paper_num[y][x - 1])
        answer = max(answer, total + temp)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = True
            DFS(ny, nx, n + 1, total + paper_num[ny][nx], i)
            # i=0: 좌, i=1:우, i=2:상, i=3:하
            visited[ny][nx] = False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
N, M = map(int, input().split())
paper_num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, paper_num[i][j], None)
        visited[i][j] = False
print(answer)
