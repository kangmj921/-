# 정점의 개수가 최대 10^6이므로 그래프의 모든 정점을 깊이 우선 탐색하면서
# 해당 정점을 선택했을 때, 선택하지 않았을 때 얼리어답터의 수를 저장하고
# 깊이를 올라오면서 저장된 값을 참조하면서
# 최소의 얼리어답터 수를 찾는다.
import sys
sys.setrecursionlimit(10 ** 9)


def DFS(start_node):
    visit[start_node] = 1
    for v in people_list[start_node]:
        if not visit[v]:
            DFS(v)
            dp_list[start_node][0] += dp_list[v][1]  # 현재 깊이의 노드를 선택하지 않았을 경우
            # 다음 인접한 노드는 무조건 얼리어답터여야 현재 깊이의 노드도 자신의 친구가
            # 얼리어답터일 수 있음.
            dp_list[start_node][1] += min(dp_list[v][0], dp_list[v][1])
            # 현재 깊이의 노드가 선택되었을 경우
            # 다음 인접한 노드는 얼리어답터일 수 있고 아닐 수도 있음.
            # 이 중 최소 얼리어답터 수 값을 저장함.


N = int(input())
people_list = [[] for _ in range(N + 1)]
dp_list = [[0, 1] for _ in range(N + 1)]
visit = [0] * (N + 1)
# 각 정점 별로, [선택되지 않았을때 얼리어탑터의 수, 선택되었을때 얼리어탑터의 수]를 저장하는 dp_list
#
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    people_list[u].append(v)
    people_list[v].append(u)
DFS(1)
print(min(dp_list[1][0], dp_list[1][1]))
