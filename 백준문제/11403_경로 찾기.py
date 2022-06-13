def search(start):
    for i in graph[start]:
        next_start = i
        if not visit[i] and G[start][i]:
            visit[i] = 1
            search(next_start)


N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
for i in range(len(G)):
    for j in range(len(G[i])):
        if G[i][j]:
            graph[i].append(j)
for i in range(len(G)):
    visit = [0] * N
    search(i)
    for j in range(len(G[i])):
        if visit[j]:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
