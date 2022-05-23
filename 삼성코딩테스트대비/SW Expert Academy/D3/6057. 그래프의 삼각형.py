def DFS(index, num_of_G, start):
    global answer
    # print(index, visited)
    if num_of_G == 3:
        if graph[index][start]:
            answer += 1
        return
    for j in range(index + 1, len(graph[index])):
        if not visited[index][j] and graph[index][j]:
            visited[index][j] = 1
            DFS(j, num_of_G + 1, start)
            visited[index][j] = 0
    return


for T in range(int(input())):
    N, M = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    answer = 0
    for _ in range(M):
        x, y = map(int, input().split())
        graph[y][x], graph[x][y] = 1, 1
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, len(graph)):
        DFS(i, 1, i)
    print("#{} {}".format(T + 1, answer))
