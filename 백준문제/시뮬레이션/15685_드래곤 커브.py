
# 오른쪽 : 0, 위쪽 : 1, 왼쪽 : 2, 아래쪽 : 3
dict_direction = {0: 1, 1: 2, 2: 3, 3: 0}  # 시작방향이 n인 드래곤 커브를 90도 회전하면 어떤 방향으로 되는지 나타내는 딕셔너리
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
board = [[0] * 101 for _ in range(101)]
visit = [[0] * 101 for _ in range(101)]
answer = 0
N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())
    stack = []
    # 드래곤 커브 n세대는 2 ^ n 개 만큼의 선분이 있다.
    board[y][x] = 1
    stack.append(d)
    ny, nx = y + dy[d], x + dx[d]
    board[ny][nx] = 1
    y, x = ny, nx
    if g >= 1:
        for i in range(g):
            for prev in range(len(stack) - 1, -1, -1):
                next_direction = dict_direction[stack[prev]]
                stack.append(next_direction)
            for j in range(len(stack) // 2, len(stack)):
                y = y + dy[stack[j]]
                x = x + dx[stack[j]]
                board[y][x] = 1
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
            answer += 1
print(answer)
