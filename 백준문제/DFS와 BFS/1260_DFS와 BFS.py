from collections import deque


def DFS(start_node):
    visited[start_node] = 1
    print(start_node + 1, end=" ")
    for i in range(len(graph[start_node])):
        if visited[graph[start_node][i]] == 0:
            DFS(graph[start_node][i])


def BFS(start_node):
    visited2 = [0] * N
    queue = deque()
    queue.append(start_node)
    visited2[start_node] = 1
    while queue:
        next_node = queue.popleft()
        print(next_node + 1, end=" ")
        for i in graph[next_node]:
            if visited2[i] == 0:
                visited2[i] = 1
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for i in range(N)]
visited = [0] * N
for i in range(M):
    start, end = map(int, input().split())
    graph[start - 1].append(end - 1)
    graph[end - 1].append(start - 1)
for i in graph:
    i.sort()
DFS(V-1)
print('')
BFS(V-1)
