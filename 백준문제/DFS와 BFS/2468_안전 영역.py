# 비의 양에 따라서 비의 양과 같거나 낮은 곳은 물에 잡기게 된다.
# 잠기지 않은 노드 그룹의 개수를 찾는 문제이다.
# 비가 온 높이별로 방문한 노드를 확인하기 위해 방문 기록 리스트를 N * N * depth로 만들고
# 현재 비의 높이에서 방문하지 않았고 높이가 비의 높이보다 높은 곳들을 bfs로 찾으면 그것이 곧 한 영역이 된다.
from collections import deque


def bfs(y, x, v, d):
    queue = deque()
    queue.append((y, x))
    v[d][y][x] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or nx >= N or ny >= N or v[d][ny][nx] or swamp_list[ny][nx] <= d:
                continue
            v[d][ny][nx] = True
            queue.append((ny, nx))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
# 2 <= N <= 100
swamp_list = [list(map(int, input().split())) for _ in range(N)]
visit_list = [[[False for _ in range(N)] for _ in range(N)] for _ in range(101)]
# 1 <= 높이 <= 100
depth = 0
answer = 0
while depth <= 100:
    count = 0
    for i in range(N):
        for j in range(N):
            if not visit_list[depth][i][j] and swamp_list[i][j] > depth:
                bfs(i, j, visit_list, depth)
                count += 1
    answer = max(answer, count)
    depth += 1
print(answer)
