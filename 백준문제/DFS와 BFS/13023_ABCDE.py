# DFS를 이용해서 탐색의 깊이가 4이면, 5개의 노드를 방문한 것이므로
# 방문한 노드의 번호와 관계 없이 A, B, C, D, E가 문제의 조건에 맞는 친구 관계를
# 가졌다고 판단한다.
# 탐색 과정 중에 한 번 깊이가 4인 탐색을 하게 되면
# 더 이상 하지 않게 백트래킹을 해서 실행 시간을 줄인다.

def DFS(start, depth):
    print(start, depth)
    if depth == 4:
        global answer  # 탐색 성공 여부 전역 변수로 선언
        answer = True
        return
    visited[start] = True
    for next_node_number in graph[start]:
        if not visited[next_node_number]:
            DFS(next_node_number, depth + 1)
    if not answer:  # 실패 했으면 다른 경로도 탐색할 수 있도록 방문 정보 삭제
        visited[start] = False
    return


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
answer = False
for i in range(N):
    if not answer:
        visited = [False] * N
        DFS(i, 0)
    else:
        break
print(1 if answer else 0)
