def check_true(y, x):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    for i in range(8):
        num = 1
        for j in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if game_board[ny][nx] == 'o':
                    num += 1
                    x, y = nx, ny
            else:
                continue
        if num == 5:
            return True
    return False


for T in range(int(input())):
    answer, check = "NO", False
    N = int(input())
    game_board = []
    for _ in range(N):
        game_board.append(input().rstrip('\n'))
    for i in range(N):
        if check:
            break
        for j in range(N):
            if game_board[i][j] == 'o':
                if check_true(i, j):
                    answer, check = "YES", True
                    break
    print("#{} {}".format(T + 1, answer))
