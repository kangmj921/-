def DFS(start_node, dir):
    global answer
    answer = max(answer, dir)
    visited[start_node] = 1
    for i in graph[start_node]:
        if not visited[i]:
            DFS(i, dir + 1)
    visited[start_node] = 0


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    answer = 0
    for i in range(1, N + 1):
        DFS(i, 1)
    print("#{} {}".format(tc + 1, answer))
