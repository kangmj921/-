def check_movable(x, y):
    if 0 <= x <= W - 1 and 0 <= y <= H - 1 and game_board[y][x] == '.':
        return True
    else:
        return False


def move(command, x, y):
    nx, ny = x, y
    if command == 'U':
        game_board[y][x] = '^'
        if check_movable(x, y - 1):
            game_board[y][x] = '.'
            nx, ny, game_board[ny][nx] = x, y - 1, '^'
    elif command == 'D':
        game_board[y][x] = 'v'
        if check_movable(x, y + 1):
            game_board[y][x] = '.'
            nx, ny, game_board[ny][nx] = x, y + 1, 'v'
    elif command == 'L':
        game_board[y][x] = '<'
        if check_movable(x - 1, y):
            game_board[y][x] = '.'
            nx, ny, game_board[ny][nx] = x - 1, y, '<'
    else:
        game_board[y][x] = '>'
        if check_movable(x + 1, y):
            game_board[y][x] = '.'
            nx, ny, game_board[ny][nx] = x + 1, y, '>'
    return nx, ny


def shoot(x, y):
    if game_board[y][x] == '^':
        for i in range(y - 1, -1, -1):
            if game_board[i][x] in '*#':
                if game_board[i][x] == '*':
                    game_board[i][x] = '.'
                break
    elif game_board[y][x] == 'v':
        for i in range(y + 1, H):
            if game_board[i][x] in '*#':
                if game_board[i][x] == '*':
                    game_board[i][x] = '.'
                break
    elif game_board[y][x] == '<':
        for i in range(x - 1, -1, -1):
            if game_board[y][i] in '*#':
                if game_board[y][i] == '*':
                    game_board[y][i] = '.'
                break
    else:
        for i in range(x + 1, W):
            if game_board[y][i] in '*#':
                if game_board[y][i] == '*':
                    game_board[y][i] = '.'
                break


T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    game_board = [list(input().rstrip('\n')) for _ in range(H)]
    N = int(input())
    for i in range(H):
        for j in range(W):
            if game_board[i][j] in '^v<>':
               x, y = j, i
    for c in input().rstrip('\n'):
        if c in 'UDLR':
            x, y = move(c, x, y)
        else:
            shoot(x, y)
    print("#{} ".format(tc + 1), end='')
    for i in range(H):
        for j in range(W):
            print(game_board[i][j], end='')
        print()
