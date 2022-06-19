from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for TC in range(int(input())):
    N = int(input())
    answer = 10 ** 9
    map_list = [list(map(int, input().rstrip())) for _ in range(N)]
    time_list = [[0] * len(map_list[0]) for _ in range(N)]
    visit = [[False] * len(map_list[0]) for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    visit[0][0] = True
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    time_list[ny][nx] = time_list[y][x] + map_list[ny][nx]
                    queue.append((ny, nx))
                else:
                    if time_list[ny][nx] > time_list[y][x] + map_list[ny][nx]:
                        time_list[ny][nx] = time_list[y][x] + map_list[ny][nx]
                        queue.append((ny, nx))
    print("#{} {}".format(TC + 1, time_list[N - 1][N - 1]))
