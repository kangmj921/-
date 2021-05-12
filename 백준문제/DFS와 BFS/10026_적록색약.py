from collections import deque


def BFS(R_G):
    result = 0
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    last_word = graph[0][0]
    queue.append((0, 0))
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny <= N:
                pass
    return result


N = int(input())
graph = [list(input().rstrip('\n')) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R_G_YES = BFS(True)
R_G_NO = BFS(False)
print(R_G_NO, R_G_YES)
