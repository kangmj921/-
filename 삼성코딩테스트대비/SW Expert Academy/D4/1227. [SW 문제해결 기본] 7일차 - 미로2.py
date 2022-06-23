from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(10):
    TC = int(input())
    answer = 0
    maze = [list(map(int, input().rstrip())) for _ in range(100)]
    visit = [[False] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                start = (i, j)
            elif maze[i][j] == 3:
                goal = (i, j)
    queue = deque()
    queue.append(start)
    visit[start[0]][start[1]] = True
    while queue:
        y, x = queue.popleft()
        if (y, x) == goal:
            answer = 1
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 100 and 0 <= nx < 100:
                if not visit[ny][nx] and maze[ny][nx] != 1:
                    visit[ny][nx] = True
                    queue.append((ny, nx))
    print("#{} {}".format(TC, answer))
