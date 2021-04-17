import sys
sys.setrecursionlimit(10**6)


def DFS(y, x):
    if y < 0 or y >= N or x < 0 or x >= M:
        return False
    if graph[y][x] == 1 and visited[y][x] == 0:
        visited[y][x] = 1
        DFS(y + 1, x)
        DFS(y - 1, x)
        DFS(y, x - 1)
        DFS(y, x + 1)
        return True
    return False


T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    visited = [[0] * M for i in range(N)]
    result = 0
    for i in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if DFS(i, j):
                result += 1
    print(result)
