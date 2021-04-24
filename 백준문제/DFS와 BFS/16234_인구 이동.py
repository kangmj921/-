# 최대 50*50 크기의 2차원 리스트를 한 원소씩 돌며 모든 연합을 찾고,
# 같은 연합끼리 인구를 동일하게 분배하는 것을 모든 원소에 대해 돌면서 한다.
# 인구 이동 1번 마다 최악 O(2500 + 연합에 포함된 나라의 개수)의 시간복잡도를 가짐.
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(start_point, c):
    queue = deque()
    queue.append(start_point)
    population_move = 1
    result_sum = global_map[start_point[0]][start_point[1]]
    visited[start_point[0]][start_point[1]] = c
    united = [start_point]
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if L <= abs(global_map[ny][nx] - global_map[y][x]) <= R and visited[ny][nx] == -1:
                queue.append((ny, nx))
                result_sum += global_map[ny][nx]
                visited[ny][nx] = c
                united.append((ny, nx))
                population_move += 1
    for (i, j) in united:
        global_map[i][j] = result_sum // population_move
    return population_move


N, L, R = map(int, input().split())
global_map = []
result = 0
for _ in range(N):
    global_map.append(list(map(int, input().split())))
while True:
    visited = [[-1] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                solution((i, j), count)
                count += 1
    if count == N * N:
        break
    result += 1
print(result)
