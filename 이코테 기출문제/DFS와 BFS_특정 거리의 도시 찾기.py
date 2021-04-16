from collections import deque
import sys

# 모든 edge의 비용이 동일할때는 BFS를 이용하여 최단 거리를 찾을 수 있다.
# 최대 시간 복잡도는 O(N + M)이다.
def find_K(d):
    check = False
    for i in range(len(d)):
        if d[i] == K:
            print(i + 1)
            check = True
    if not check:
        print(-1)


def BFS(start_node):
    distace_list = [-1] * N
    distace_list[start_node] = 0
    queue = deque()
    queue.append(start_node)
    while queue:
        now = queue.popleft()
        for next_node in city_list[now]:
            if distace_list[next_node] == -1:
                distace_list[next_node] = distace_list[now] + 1
                queue.append(next_node)
    find_K(distace_list)


N, M, K, X = map(int, input().split())
city_list = [[] for i in range(N)]
for i in range(M):
    y, x = map(int, sys.stdin.readline().split())
    city_list[y-1].append(x-1)
BFS(X - 1)
