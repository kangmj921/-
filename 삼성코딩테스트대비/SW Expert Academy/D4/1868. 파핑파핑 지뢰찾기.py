def count_bomb(y, x):
    cnt = 0
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            cnt += board_list[ny][nx] == '*'
    return cnt


def click(y, x):
    if board_list[y][x] == '.':
        board_list[y][x] = count_bomb(y, x)
        if board_list[y][x] == 0:
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N:
                    click(ny, nx)


dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
for T in range(int(input())):
    N = int(input())
    board_list = [list(input().rstrip()) for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(N):
            if board_list[i][j] == '.' and not count_bomb(i, j):
                answer += 1
                click(i, j)
    answer += sum(board_list[y][x] == '.' for x in range(N) for y in range(N))
    print("#{} {}".format(T + 1, answer))
