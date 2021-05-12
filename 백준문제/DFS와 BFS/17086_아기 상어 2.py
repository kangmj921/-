# 그래프를 돌면서 아기 상어들이 있는 좌표를 모두 queue에 넣고
# 큐의 원소를 하나씩 빼면서 아기 상어들을 한 번씩 이동시킨다.
# 그렇게 하게 되면 모든 좌표에 대해서 모든 아기 상어들 과의 최소 거리를
# 나타낼 수 있고, 이 최소 거리들 중 최댓값을 출력하면 된다.
from collections import deque


def search_BFS():
    while queue:
        p_y, p_x = queue.popleft()
        for i in range(8):
            ny = p_y + dy[i]
            nx = p_x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[p_y][p_x] + 1
                    queue.append((ny, nx))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1
search_BFS()
max_result = 0
for i in range(N):
    for j in range(M):
        max_result = max(visited[i][j] - 1, max_result)
print(max_result)
