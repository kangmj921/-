# 넓이 우선 탐색으로 풀 때는, 방문했던 적이 없는
# 이동할 수 있는 홈으로 이동해본다.
# 이때 y좌표가 T인 경우엔 정상에 올랐으니, 이동 횟수 출력
# 만약 큐가 비었는데도 y좌표가 T보다 작다면, 정상에 오를 수 없으니
# -1 출력.
# DFS나 BFS로 구현할 경우, 시간복잡도는
# 다음 홈으로 가는 경우의 수는 최대 24가지이고, 최대 정점의 수는
# 50,000이므로, 최악 시간복잡도로는 O(24 * (50,000 + 50,000))이 걸릴 것이다.
import sys
from collections import deque


def BFS(g):
    queue = deque()
    visited = [[50001] * len(g[0]) for _ in range(len(g))]
    visited[0][0] = 0
    queue.append((0, 0))
    check = False
    while queue:
        p_x, p_y = queue.popleft()
        if p_y == T:
            check = True
            print(visited[p_y][p_x])
            return check
        for i in range(-2, 3):
            for j in range(-2, 3):
                n_x = p_x + i
                n_y = p_y + j
                if 0 <= n_x < len(g[0]) and 0 <= n_y < len(g):
                    if graph[n_y][n_x] == 1 and visited[n_y][n_x] == 50001:
                        queue.append((n_x, n_y))
                        visited[n_y][n_x] = min(visited[n_y][n_x], visited[p_y][p_x] + 1)
    return check


n, T = map(int, input().split())
point_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point_list.sort()
graph = [[0] * (point_list[-1][0] + 1) for _ in range(T + 1)]
for x, y in point_list:
    graph[y][x] = 1
if not BFS(graph):
    print(-1)
