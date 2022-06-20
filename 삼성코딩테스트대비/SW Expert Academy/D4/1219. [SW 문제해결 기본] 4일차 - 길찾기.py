from collections import deque


for _ in range(10):
    T, P = map(int, input().split())
    n_list = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visit = [False] * 100
    for i in range(0, len(n_list), 2):
        start, end = n_list[i], n_list[i + 1]
        graph[start].append(end)
    # print(graph)
    answer = 0
    queue = deque()
    queue.append(0)
    visit[0] = True
    while queue:
        start = queue.popleft()
        if start == 99:
            answer = 1
        for i in range(len(graph[start])):
            next_node = graph[start][i]
            if not visit[next_node]:
                visit[next_node] = 1
                queue.append(next_node)
    print("#{} {}".format(T, answer))
