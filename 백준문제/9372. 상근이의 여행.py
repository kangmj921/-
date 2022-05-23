# DFS BFS와 완전탐색은 다르다. 혼용해서 사용하지 말자.
import sys


def DFS(node, answer):
    visited[node] = 1
    for n in map_list[node]:
        if not visited[n]:
            answer = DFS(n, answer + 1)
    return answer


for T in range(int(input())):
    N, M = map(int, sys.stdin.readline().split())
    map_list = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        map_list[start].append(end)
        map_list[end].append(start)
    answer = DFS(1, 0)
    print(answer)
