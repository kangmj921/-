from collections import deque


def BFS(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if maze[y][x] == 0:
                continue
            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))
    return maze[N-1][M-1]


N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().rstrip('\n'))))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for i in range(N)]
print(BFS(0, 0))
