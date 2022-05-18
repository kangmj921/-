for tc in range(int(input())):
    N, M = map(int, input().split())
    game_board = [[0] * (N + 1) for _ in range(N + 1)]
    game_board[N // 2][N // 2], game_board[N // 2 + 1][N // 2 + 1] = 2, 2
    game_board[N // 2][N // 2 + 1], game_board[N // 2 + 1][N // 2] = 1, 1
    b, r = 0, 0
    dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, 1, 1, -1]
    for _ in range(M):
        x, y, c = map(int, input().split())
        game_board[y][x] = c
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            remember_y_x = []
            while True:
                if nx < 1 or N < nx or ny < 1 or N < ny:
                    remember_y_x = []
                    break
                if not game_board[ny][nx]:
                    remember_y_x = []
                    break
                if game_board[ny][nx] == c:
                    break
                else:
                    remember_y_x.append((nx, ny))
                nx += dx[i]
                ny += dy[i]
            for r_x, r_y in remember_y_x:
                game_board[r_y][r_x] = c
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if game_board[i][j] == 2:
                r += 1
            if game_board[i][j] == 1:
                b += 1
    print("#{} {} {}".format(tc + 1, b, r))
