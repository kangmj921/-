# 연구소의 크기가 최대 8 * 8이라 원소의 개수는 최대 64개이므로 모든 0인 경우에 대해 벽을
# 세우는 경우의 수가 최악의 경우 64C3으로 41664가지으므로, 시간제한에 걸리지않을것이다.
# 그리고 위의 경우 모두에 대해 바이러스 가 퍼진 후 영역을 DFS나 BFS로 구할 것이다.
import copy
from collections import deque


def combinations_to_3(l, n):
    result_list = []
    for i in range(0, len(l) - (n - 1)):
        for j in range(i + 1, len(l)-(n - 2)):
            for k in range(j + 1, len(l) - (n - 3)):
                result_list.append([l[i], l[j], l[k]])
    return result_list


def area_to_BFS(t):
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0]* M for i in range(N)]
    queue = deque()
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == 2:
                queue.append((i, j))
    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if t[ny][nx] == 1:
                continue
            if t[ny][nx] == 0 and visited[ny][nx] == 0:
                t[ny][nx] = 2
                visited[ny][nx] = 1
                queue.append((ny, nx))
    for i in range(N):
        for j in range(M):
            if t[i][j] == 0:
                result += 1
    return result


N, M = map(int, input().split())
lab_map = []  # 바이러스의 개수는 2 ~ 10, 0의 개수는 3개 이상, 새로 세우는 벽의 개수는 3개
for i in range(N):
    lab_map.append(list(map(int, input().split())))
to_build_wall_list = []
max_area = 0
for i in range(N):
    for j in range(M):
        if lab_map[i][j] == 0:
            to_build_wall_list.append((i, j))
to_build_wall_list = combinations_to_3(to_build_wall_list, 3)
for a, b, c in to_build_wall_list:
    temp_map = copy.deepcopy(lab_map)
    temp_map[a[0]][a[1]], temp_map[b[0]][b[1]], temp_map[c[0]][c[1]] = 1, 1, 1
    max_area = max(max_area, area_to_BFS(temp_map))
print(max_area)
