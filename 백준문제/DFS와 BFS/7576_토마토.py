from collections import deque


def BFS(q):
    result = -1
    time = 0
    visited2 = [queue[-1]]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                graph[ny][nx] = 1
                visited[ny][nx] = 1
                queue.append((ny, nx))
        if len(queue) != 0 and (y, x) == visited2[-1]:
            visited2.append(queue[-1])
            result += 1
    check = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                check = True
    if check:
        return -1
    else:
        return result + 1


M, N = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for i in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
a = []
queue = deque()
check = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
        elif graph[i][j] == 0:
            check = True
if check:
    print(BFS(queue))
else:
    print(0)
