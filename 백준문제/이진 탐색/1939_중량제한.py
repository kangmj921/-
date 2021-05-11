# 이진탐색이나 BFS로 접근이 가능할 것이다. 하지만 BFS의 경우는
# 그래프를 인접 행렬로 구현하게 되면 최악 O(100,000 * 100,000)으로
# 시간 제한을 만족하지 못한다. 따라서 linked list로 구현을 해야
# O(정점의 개수 + 간선의 개수)만 큼이 될 것이다.
# 이진탐색으로 어떻게 구현을 해야 할지 생각해봐야 될 것 같다.
# 제일 큰 중량제한을 가지는 경우와 제일 작은 중량 제한을 가지는 경우로 해서
# 공장이 있는 두 섬을 연결하는 경로는 항상 존재하니까 이진탐색으로
# 값을 찾아나가면서 그 중량으로 a->b로 갈 수 있는지 확인하고 만약 된다면,
# 최대 중량을 크게 해보고 없다면 작게 해보는 식으로 해볼 것이다.
# 그렇게 한다면, a->b로 가는 과정을 그래프 탐색식으로 구현을 하게 되면,
# 이진 탐색이 log2(1,000,000,000)번 된다고 햇을떄,
# 각 이진탐색 마다 최악 O(정점의 개수 + 간선의 개수)이 일어난다
# 따라서 최악 시간 복잡도는 O(log2(1,000,000,000)*(V + E))
import sys
from collections import deque


def BFS_check(start, end, limit, g):
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        p_s = q.popleft()
        if p_s == end: return True
        for next_start, next_limit in g[p_s]:
            if next_limit >= limit and visited[next_start] == 0:
                visited[next_start] = 1
                q.append(next_start)
    return False


N, M = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    start, end, limit = map(int, sys.stdin.readline().split())
    graph[start].append([end, limit])
    graph[end].append([start, limit])
a, b = map(int, input().split())
min_limit, max_limit = 1, 1000000000
while min_limit <= max_limit:
    visited = [0 for _ in range(N + 1)]
    mid = (min_limit + max_limit) // 2
    if BFS_check(a, b, mid, graph):
        min_limit = mid + 1
    else:
        max_limit = mid - 1
print(max_limit)
