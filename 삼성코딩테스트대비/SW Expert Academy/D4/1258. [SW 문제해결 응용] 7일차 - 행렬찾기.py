from collections import deque


def bfs_search(y, x):
    queue = deque()
    queue.append((y, x, 1, 1))
    visit_list[y][x] = True
    while queue:
        y, x, row, col = queue.popleft()
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= N or nx >= N:
                continue
            if not visit_list[ny][nx] and store_list[ny][nx]:
                visit_list[ny][nx] = True
                if i == 0:
                    queue.append((ny, nx, row, col + 1))
                else:
                    queue.append((ny, nx, row + 1, col))
    return [row, col]


dx = [1, 0]
dy = [0, 1]
for TC in range(int(input())):
    N = int(input())
    store_list = [list(map(int, input().split())) for _ in range(N)]
    visit_list = [[False] * N for _ in range(N)]
    dp_list = []
    n = 0
    answer = []
    for i in range(N):
        for j in range(N):
            if store_list[i][j] and not visit_list[i][j]:
                n += 1
                dp_list.append(bfs_search(i, j))
    dp_list.sort(key=lambda x: (x[0] * x[1], x[0]))
    for row, col in dp_list:
        answer.append(row)
        answer.append(col)
    print("#{} {}".format(TC + 1, n), *answer)
