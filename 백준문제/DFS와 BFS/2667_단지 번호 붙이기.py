def DFS(y, x, n):
    global num_of_apart
    if y < 0 or y >= N or x < 0 or x >= N:
        return False
    if map_list[y][x] == 1 and visited[y][x] == 0:
        num_of_apart += 1
        visited[y][x] = 1
        DFS(y + 1, x, num_of_apart)
        DFS(y - 1, x, num_of_apart)
        DFS(y, x + 1, num_of_apart)
        DFS(y, x - 1, num_of_apart)
        return True
    return False


N = int(input())
map_list = []
result = 0
result_list = []
num_of_apart = 0
visited = [[0] * N for i in range(N)]
for i in range(N):
    map_list.append(list(map(int, input().rstrip('\n'))))
for i in range(N):
    for j in range(N):
        if DFS(i, j, num_of_apart):
            result += 1
            result_list.append(num_of_apart)
            num_of_apart = 0
print(result)
result_list.sort()
for i in result_list:
    print(i)
