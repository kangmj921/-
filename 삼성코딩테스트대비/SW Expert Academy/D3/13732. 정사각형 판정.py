def search(y, x):
    down, right = 0, 0
    check = False
    for i in range(y, N):
        if board_list[i][x] == '#':
            down += 1
        else:
            break
    for i in range(y, y + down):
        if not check:
            for j in range(x, x + down):
                if j < N and board_list[i][j] == '#':
                    visited[i][j] = 1
                else:
                    check = True
                    break
    if not check:
        return True
    else:
        return False


for T in range(int(input())):
    N = int(input())
    board_list = list(input().rstrip() for _ in range(N))
    visited = [[0] * N for _ in range(N)]
    answer = []
    for i in range(len(board_list)):
        for j in range(len(board_list[i])):
            if board_list[i][j] == '#' and not visited[i][j]:
                answer.append(search(i, j))
    if len(answer) != 1 or not answer[-1]:
        answer = 'no'
    else:
        answer = 'yes'

    print("#{} {}".format(T + 1, answer))
