from collections import deque


for _ in range(int(input())):
    L = int(input())
    chess = [[0] * L for _ in range(L)]
    present = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))
    visited = [[0] * L for _ in range(L)]
    dx = [-1, -1, 1, 1, 2, 2, -2, -2]
    dy = [2, -2, -2, 2, -1, 1, -1, 1]
    queue = deque()
    queue.append(present)
    chess[present[0]][present[1]] = 1
    while queue:
        y, x = queue.popleft()
        if (y, x) == goal:
            break
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= L or nx < 0 or nx >= L:
                continue
            if chess[ny][nx] == 0:
                chess[ny][nx] = chess[y][x] + 1
                queue.append((ny, nx))
    print(chess[goal[0]][goal[1]] - 1)
