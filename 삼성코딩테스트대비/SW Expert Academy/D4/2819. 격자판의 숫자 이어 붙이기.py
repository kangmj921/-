from collections import deque


def bfs_search(y, x, c):
    global answer
    queue = deque()
    queue.append((y, x, c))
    while queue:
        y, x, cnt = queue.popleft()
        if len(cnt) == 7:
            result = int(cnt)
            answer.append(result)
            # if not hash_table[result]:
            #     hash_table[result] += 1
            #     answer += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 4 and 0 <= nx < 4 and len(cnt) <= 6:
                queue.append((ny, nx, cnt + board[ny][nx]))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for T in range(int(input())):
    # hash_table = [0] * (10 ** 8)
    answer = []
    board = [list(input().split()) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            bfs_search(i, j, board[i][j])
    answer = set(answer)
    print("#{} {}".format(T + 1, len(answer)))
