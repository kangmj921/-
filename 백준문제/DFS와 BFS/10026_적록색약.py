from collections import deque


def BFS(y, x, target, R_G):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[ny][nx] == 0:
                    if R_G:
                        if target in 'RG' and graph[ny][nx] in 'RG':
                            visited[ny][nx] = 1
                            queue.append((ny, nx))
                        else:
                            if graph[ny][nx] == target:
                                visited[ny][nx] = 1
                                queue.append((ny, nx))
                    if not R_G:
                        if graph[ny][nx] == target:
                            visited[ny][nx] = 1
                            queue.append((ny, nx))


N = int(input())
graph = [list(input().rstrip('\n')) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R_G_YES, R_G_NO = 0, 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, graph[i][j], False)
            R_G_NO += 1
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, graph[i][j], True)
            R_G_YES += 1
print(R_G_NO, R_G_YES)
