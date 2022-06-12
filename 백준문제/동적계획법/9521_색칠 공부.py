# K는 색의 종류의 수, N은 그림 리스트를 나타내는 수
# f_list는 i번 그림과 다른 색으로 색칠하기 위해 주어진 수
# 만약 i가 f_list의 i와 같은 경우 아무 제한 없이 i번 그림 색칠 가능
# N과 K의 범위가 10^6까지이므로, 각 원소를 일일히 확인하는 것은
# 시간이 오래 걸릴 것이다.

# 어떤 그룹의 첫번째로 만난 i번 그림이 색칠할 수 있는 경우의 수는 N가지로,
# i번 그림도 fi번 그림과 다른 색으로
# 칠해야 하지만, fi번 그림의 색 가지 수를 1가지 빼서 정해주면 되는 일이므로
# i번 그림에 총 N 가지 색을 칠할 수 있다고 가정한다.
#
# fi = j이면 i번 노드가 j번 노드로 간선을 가지는 그래프 구조라고 가정했을 때,
# i는 start_node, j는 target_node, dp[i]는 i번 그림의 색깔 경우의 수 라고 정의한다.
# fi = j일때, fi = j = i를 만족할시 즉, i번 노드의 간선이 자기 자신에게 연결되어 있는 노드에
# 연결되는 경우 dp[i]는 dp[j] - 1을 가지고, fk -> i인 k 노드는 dp[i]의 값을 가진다.
# fj != i 일시엔, dp[i] = dp[j] - 1

# 모든 그림이 같은 그룹에 속해 있지는 않을 것이다.
# 그룹을 어떻게 판단할까가 문제임..처음 시작하는 dp[j]값이 존재하지 않을때,
# 해당 그룹에 속한 모든 노드를 돌기 위해 깊이 우선 탐색을 진행한다.
# 모든 노드를 탐사한 후, 가장 마지막에 탐사한 노드를 K개의 색 모두를 칠하는 첫 번째
# 그림이라고 한다. 그리고 해당 노드에서 다시 연결된 노드들이 dp_list 값을 구할 수 있도록함.

# 각 그룹 끼리의 경우의 수는 동시에 일어나는 일은 아니니까, 모두 곱하지 않고, 그룹끼리는
# 최종 경우의 수는 서로 합셈한다.

# 메모리 초과라는 예상치 못한 결과를 받았다.
# 정점의 수가 최대 10^6, 이를 연결하는 간선의 수도 최대 10^6개다.
# 모든 간선을 돌며 정점을 탐색하는 DFS의 시간 복잡도는 O(V * E)로 오래 걸리기 때문에
# dp를 사용해서 dp의 값이 할당되지 않은 초기에 그룹을 구성하는 노드와 간선을 모두 도는 과정에서
# 재귀로 인해 메모리 초과가 나거나, dp_list 의 원소를 모두 곱하는 과정에서 발생하는 것 같다.


# 결국 모든 순회하는 그래프 그룹들에 대해, 경우의 수를 구해야하는 것이 목적임.
# 이 과정을 좀 더 간단하게 해야 함. 1번 노드부터 N번 노드 까지 이루어진 그룹이 있을때,
# (이 때, 한 그룹은 한 노드에서 출발해서 모든 노드로 순회가 가능한 상태임.)
# 1번 노드의 경우의 수 = K, 2번 노드에서 부터 N번 노드 까지의 경우의 수 = K - 1인데,
# 1번 노드와 N - 1 노드가 같은 색상을 가질 수도, 아닐 수도 있다.
# 같은 색상을 가질 경우, N번 노드의 경우의 수는 K - 1
# 아닐 경우, K - 2
# 즉, d[N] = d[N - 2] * (K - 1) + d[N - 1] * (K - 2)

# 그룹에 속하지 않는 노드들의 경우의 수는 K - 1이다.(fi와는 다른 색으로 칠해야함.)
# 검색해서 다른 방법도 사용해보았지만, 메모리 초과에 걸린다. 파이썬으로는 불가능한 것같다.
import sys
sys.setrecursionlimit(10 ** 9)


def search(start_node):  # start_node = i, target_node = j, paint_graph[][0] = f
    target_node = paint_graph[start_node][0]
    visit[start_node] = 1
    if target_node == start_node:  # start_node 가 자기 자신으로 가는 간선을 가지고 있음.
        dp_list[start_node] = K % mod  # 아무런 제한없이 색칠할 수 있으므로, 경우의 수 K
    else:  # start_node 가 다른 노드로 가는 간선을 가지고 있음.
        if not dp_list[target_node]:  # dfs 로 해당 그룹 모두 방문할 때 까지 재귀 이용
            if not visit[target_node]:
                search(target_node)
                if not dp_list[target_node] and visit[target_node]:  # 해당 그룹을 모두
                    # 방문하고 난 후, 마지막 노드는 K개의 색을 모두 칠할 수 있다.
                    dp_list[start_node] = K % mod
                    stack.append(target_node)
                search(start_node)  # 그리고 해당 노드에서 다시 재귀를 돌려서 그룹 내
                # 모든 노드에 대해 경우의 수를 구하게 함.
        else:
            if paint_graph[target_node][0] == target_node:  # fi = j = i일 때, fk -> i인
                # k 노드를 reverse_graph[i]에서 바로 찾을 수 있다.
                dp_list[start_node] = (dp_list[target_node] - 1) % mod
                k = reverse_graph[start_node][0]
                dp_list[k] = dp_list[start_node] % mod
            else:  # fi -> j일때, j != i인 경우 dp[i] = dp[j] - 1
                if dp_list[target_node]:
                    dp_list[start_node] = (dp_list[target_node] - 1) % mod
    print(start_node, target_node, dp_list[start_node], dp_list[target_node])


def dfs(idx, cnt):
    if visit[idx]:
        if first_visit[idx] != start_node:
            return 0
        return cnt - visit[idx]
    visit[idx] = cnt
    first_visit[idx] = start_node
    return dfs(f_list[idx], cnt + 1)


N, K = map(int, sys.stdin.readline().split())
f_list = [0] + list(map(int, sys.stdin.readline().split()))
paint_graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]
visit = [0] * (10 ** 6 + 1)
first_visit = [0] * (10 ** 6 + 1)
mod = 1000000007
answer = 1
dp_list = [0] * (N + 1)
stack = []
check = True
# if not check:
#     stack = []
#     for i in range(1, N + 1):
#         idx, f_i = i, f_list[i - 1]
#         paint_graph[idx].append(f_i)
#         reverse_graph[f_i].append(idx)
#     for node in range(1, N + 1):
#         if not dp_list[node]:
#             search(node)
#     if not stack:
#         for i in range(1, N + 1):
#             answer *= dp_list[i] % mod
#     else:
#         result, start = [], 1
#         for i in range(len(stack)):
#             end = stack[i]
#             for j in range(start, end + 1):
#                 answer *= dp_list[j] % mod
#             result.append(answer)
#             answer = 1
#             start = end + 1
#         answer = sum(result)
dp_list = [0] * (10 ** 6 + 1)
dp_list[0], dp_list[1], dp_list[2], dp_list[3] = 1, K, K * (K - 1) % mod, K * (K - 1) * (K - 2) % mod
for i in range(4, N + 1):
    dp_list[i] = (dp_list[i - 2] * (K - 1) + dp_list[i - 1] * (K - 2))
    dp_list[i] %= mod
single_node, group_node = N, 0
for i in range(1, N + 1):
    if not visit[i]:
        start_node = i
        group_node = dfs(i, 1)

        answer *= dp_list[group_node]
        answer %= mod
        single_node -= group_node
for i in range(1, single_node + 1):
    answer *= (K - 1)
    answer %= mod
sys.stdout.write(str(answer))
