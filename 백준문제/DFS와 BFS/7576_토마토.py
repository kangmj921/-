from collections import deque


# 기존에 풀었던 BFS를 이용해서 미로 안에서 최단 거리를 구하는 문제와 유사한 방식으로 접근을 했다.
# 문제에서 요구한 것은 토마토가 모두 익기까지의 최단 날짜이므로, 하루 마다 익게되는 토마토의 위치들중
# 제일 나중에 익게될 토마토가 익게되면 하루를 넘기도록 하였다. 나머지 부분은 문제에서 명시된대로 하였다.
# 창고의 크기는 최대 1000 * 1000으로, 내가 짠 코드대로 하면 최종적으로 3 * O(1000*1000)의
# 최악 시간 복잡도가 나올 것 같다.
def BFS(q):
    result = -1
    time = 0
    visited2 = [queue[-1]]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 0 and visited[ny][nx] == 0:
                graph[ny][nx] = 1
                visited[ny][nx] = 1
                queue.append((ny, nx))
        if len(queue) != 0 and (y, x) == visited2[-1]:
            visited2.append(queue[-1])
            result += 1
    check = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                check = True
    if check:
        return -1
    else:
        return result + 1


M, N = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for i in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
a = []
queue = deque()
check = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
        elif graph[i][j] == 0:
            check = True
if check:
    print(BFS(queue))
else:
    print(0)
