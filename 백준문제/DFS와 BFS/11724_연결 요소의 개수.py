# 노드가 이루는 그룹의 수를 구하는 문제
# DFS로 방문하지 않은 노드 1개씩 탐색한다.
#
import sys


def dfs(start, depth):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1)


sys.setrecursionlimit(10 ** 6)
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, N + 1):
    if not visited[i]:
        if not graph[i]:
            answer += 1
            visited[i] = True
        else:
            dfs(i, 0)
            answer += 1

print(answer)