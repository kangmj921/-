#
# 환경 부담금을 최소화 하면서 모든 섬을 연결하려면, 모든 섬을 연결했을 때 해저터널의
# 길이를 최소화해야 한다.
# 이 길이를 최소화 하기 위해서는, greedy 한 방법을 사용하게 되면
# 임의로 방문한 섬에 대해 아직 방문하지 않은 섬들 중 거리가 제일 가까운 섬들을 선택해나가면 된다.
# 그런데 처음 시작 섬에 따라 값들이 다를 수 있으므로, 모든 섬을 출발로 해서 경로를 구해봐야 한다.
# 한 섬을 선택했을 때, 시간 복잡도는 N ^ 2 이다. 그런데 모든 섬을 출발로 해서 모든 경우를 구하면
# 최대 시간복잡도는 N * N * N으로, 이 때 최대 1000^3 이므로, 10^9 시간제한에 걸린다.

# 모든 정점을 연결해야 하고, 최소 간선의 개수는 정점의 개수 -1개 이므로, MST 알고리즘을 사용가능하다.
# MST 알고리즘으로는 kruskal, prim 알고리즘 등이 있다.
# kruskal 알고리즘은 모든 간선들을 가중치의 오름차순으로 정렬하고 순서대로 사이클을 형성하지 않는
# 간선을 선택하는데, 가중치가 낮은 것을 선택해 나가는 알고리즘이다.
# 시간 복잡도는 O(elog2e)이므로, 간선의 개수가 적을 수록 좋다.
# prim 알고리즘의 경우, 최소 간선으로 연결된 정점을 선택해가면서, 모든 N 개의 노드가 연결되는
# 즉, N - 1개의 간선을 가질때까지 반복한다. 시간 복잡도는 O(N^2)이므로 노드의 수가 적을 수록 좋다.

# 이 문제의 경우 간선의 개수는 딱히 주어져 있지 않고, 간선의 가중치를 알기 위해선,
# 한 개의 노드를 제외한 나머지 노드들에 대한 거리를 모두 구해서 비교해야 한다.
# 즉 1개의 노드에 대해 최대 N - 1번의 연산이 필요하다.
#
# prim 알고리즘은 임의의 시작 정점을 하나 정하고, N개의 정점이 모두 선택될 때까지
# 방문한 정점에 인접하고 아직 방문하지 않은 정점 중 최소의 비용의 간선이 존재하는 정점을 선택
# 선택한 정점을 방문처리하는 것을 반복하는 알고리즘이다.

# 우선순위 큐도 활용이 가능하다. (방문한 정점에 인접한 정점 리스트를 우선순위 큐로 만들고 최소의 비용을
# 가지는 정점을 바로 뺴낼 수 있다.)
import math


def prim(start):
    global answer
    visit[start] = 1
    visited_list = [start]
    for _ in range(N - 1):
        min_dist, next_node = math.inf, -1
        for node in visited_list:
            for j in range(N):
                if not visit[j] and 0 < adj[node][j] < min_dist:
                    min_dist = adj[node][j]
                    next_node = j
        answer += min_dist
        visited_list.append(next_node)
        visit[next_node] = 1


for TC in range(int(input())):
    N = int(input())  # N <= 1000
    island_X = list(map(int, input().split()))  # X, Y <= 1,000,000
    island_Y = list(map(int, input().split()))
    E = float(input())
    answer = 0
    adj = [[0] * N for _ in range(N)]
    select = 0
    visit = [0] * N
    # 무방향 그래프 생성
    for i in range(N):
        for j in range(N):
            adj[i][j] = ((island_X[i] - island_X[j]) ** 2 + (island_Y[i] - island_Y[j]) ** 2) * E
            adj[j][i] = ((island_X[i] - island_X[j]) ** 2 + (island_Y[i] - island_Y[j]) ** 2) * E
    prim(0)
    print("#{} {}".format(TC + 1, round(answer)))
