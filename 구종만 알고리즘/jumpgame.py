import sys


def jump_game(board, x, y, N):
    end = False
    if x is N - 1 and y is N - 1:
        return True
    move_position = board[x][y]
    if move_position != -1:
        if not end and x < N - move_position:
            end = jump_game(board, x + move_position, y, N)
        if not end and y < N - move_position:
            end = jump_game(board, x, y + move_position, N)
        board[x][y] = -1
    return end


for C in range(int(input())):
    n = int(input())
    nums = list()
    for i in range(n):
        nums.append(list(map(int, sys.stdin.readline().split())))
    if jump_game(nums, 0, 0, n):
        print("YES")
    else:
        print("NO")
