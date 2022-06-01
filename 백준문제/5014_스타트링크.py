# 처음엔 재귀를 이용한 DFS로 하려 했는데 입력 범위가 10^6 승이라 재귀 반복 제한이 걸렸다
# queue를 이용한 BFS로 풀었다.
# 한 층에서 올라가든 내려가든 아무 선택이나 할 수 있으므로 모든 단계를 훑는 깊이 우선 탐색이
# 더 옳은 방법인 것 같다.
import math
from collections import deque


def search(present, n):
    global answer
    queue = deque()
    queue.append((present, n))
    while queue:
        s, count = queue.popleft()
        if s == G - 1:
            answer = min(answer, count)
        for i in range(2):
            n_s = s + ds[i]
            if n_s < 0 or n_s >= F:
                continue
            if not visited[n_s]:
                visited[n_s] = 1
                queue.append((n_s, count + 1))


F, S, G, U, D = map(int, input().split())
# F는 총 층수, S는 지금 있는 층, G는 목표 층, U는 한 번에 올라가는 층, D는 한 번에 내려가는 층
visited = [0] * F
visited[S - 1] = 1
ds = [U, -D]
answer = math.inf
search(S - 1, 0)
if answer == math.inf:
    print("use the stairs")
else:
    print(answer)
