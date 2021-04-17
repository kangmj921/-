from collections import deque


N, M = map(int, input().split())
graph = []
visited = [[0] * M for i in range(N)]
for i in range(N):
    graph.append(list(map(int, input().strip('\n'))))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if graph[ny][nx] == 0:
            continue
        if graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))
print(graph[N - 1][M - 1])