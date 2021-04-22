# 이분 그래프의 개념에 대해서 문제에 설명하는 것 보다 더 알아보니,
# 간선으로 연결된 각 노드의 집합을 두 집합으로 나눌 수 있으면 이분 그래프이다.
# 간선 어디에도 연결되지 않은 노드는 고려할 필요가 없다는 것을 알았다.
# 쉽게 예를 들면, (1) - (3) - (2) (4)로 된 그래프가 있다면,
# (1), (2)가 한 집합일 떄, (3)은 다른 집합이여야 하고, (4)는 상관이 없다.
# 정점의 개수가 20000개, 간선의 개수가 200000개 까지 되므로, 잘못하면 시간초과가 난다.
# BFS나 DFS로 탐색하는 과정에서 이분 그래프인지 판단을 해야 시간초과에 걸리지 않을 것이다.
# 앞선 이분 그래프의 개념에 따라 탐색을 하면서 출발 노드를 집합 1에 넣고 도착 노드를 집합 2에
# 넣고 탐색을 진행하면서 이미 집핮 2에 속한 노드를 집합 1에 넣게 될 경우, 그리고 그 반대
# 의 경우, 이분 그래프가 아니라고 판단하는 방식으로 구현을 해볼 것이다.
# 이 과정을 더 효율적으로 구현을 하기 위해서, 0으로 이루어진 노드 길이의 1차원 리스트에 대해
# 시작 노드와 도착 노드는 값이 0일 때, 각자 1, -1로 하고,
# 탐색하는 과정에서 출발 노드와 도착 노드의 값이 서로 다르게 하는데,
# ex) 출발 노드 or 도착 노드의 값이 있다면, 그 값의 반대인 값을 값이 없는 쪽으로 함.
# 만약 출발 노드와 도착 노드가 둘 다 이미 값이 이미 있는데, 같다면
# 이분 그래프가 아니라고 판단하면 될 것 같다.
# 만약 구현이 잘 된다면, 시간 복잡도는 최악 O(200,000)으로, 효율적으로 할 수 있을 것이다.
# 그런데 이 경우는, 반례가 있었다. 전혀 상관없던 간선 둘을 잇는 간선이 생기는 경우였다.
# 두 노드 모두 값이 0일 때 1, -1로 초기화 시키는 부분을 고쳐야할 것이다.
# 그래프를 먼저 그리고 한 노드 씩 너비 우선 탐색으로 해서 해결함.
# 꼼수 수지 말자.
from collections import deque
import sys


def search_BFS(g, start_node):
    q = deque()
    q.append(start_node)
    visited[start_node] = 1
    while q:
        present = q.popleft()
        for i in g[present]:
            if not visited[i]:
                visited[i] = -1 * visited[present]
                q.append(i)
            elif visited[i] == visited[present]:
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)
    visited = [0] * (V + 1)
    check = True
    for start in range(len(visited)):
        if visited[start] == 0:
            check = search_BFS(graph, start)
            if not check:
                break
    if check:
        print("YES")
    else:
        print("NO")
