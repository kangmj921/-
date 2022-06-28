# 문제의 조건을 잘 읽어 보고 코드를 꼼꼼히 확인했으면 더 빨리 풀었을 것이다...
from collections import deque


def bfs_search(y, x, s):
    queue = deque()
    queue.append((y, x, 0))
    visit_list = [[False for _ in range(N)] for _ in range(N)]
    visit_list[y][x] = True
    result = []
    while queue:
        y, x, cnt = queue.popleft()
        if 0 < ocean_list[y][x] < s:
            if not result:
                result = [(y, x, cnt)]
            else:
                if cnt < result[-1][2]:
                    result.append((y, x, cnt))
                elif cnt == result[-1][2]:
                    if y < result[-1][0]:
                        result.append((y, x, cnt))
                    elif y == result[-1][0]:
                        if x < result[-1][1]:
                            result.append((y, x, cnt))
                else:
                    break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if not visit_list[ny][nx] and ocean_list[ny][nx] <= size_of_shark:
                visit_list[ny][nx] = True
                queue.append((ny, nx, cnt + 1))
    if result:
        return [result[-1]]
    else:
        return result


dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
N = int(input())
ocean_list = [list(map(int, input().split())) for _ in range(N)]
fish_list = [0]
answer = 0
count = 0
size_of_shark = 2
for i in range(N):
    for j in range(N):
        if ocean_list[i][j] == 9:
            ocean_list[i][j] = 0
            while fish_list:
                fish_list = bfs_search(i, j, size_of_shark)
                if fish_list:
                    i, j = fish_list[-1][0], fish_list[-1][1]
                    answer += fish_list[-1][2]
                    count += 1
                    ocean_list[i][j] = 0
                    if count == size_of_shark:
                        size_of_shark += 1
                        count = 0
            break
print(answer)
