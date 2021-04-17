from collections import deque


N = int(input())
graph = [[] for i in range(N)]
visited = [0] * N
for i in range(int(input())):
    start, end = map(int, input().split())
    graph[start-1].append(end-1)
    graph[end-1].append(start-1)
start_node = 0
result = 0
queue = deque()
queue.append(start_node)
visited[start_node] = 1
while queue:
    next_node = queue.popleft()
    for i in graph[next_node]:
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
            result += 1
print(result)
