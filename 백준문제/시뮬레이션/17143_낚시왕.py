# 칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.
# 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다.
#
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
# 낚시왕이 오른쪽으로 한 칸 이동한다.
# 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 상어가 이동한다.
# 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다.
# 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.
# 두 상어가 같은 크기를 갖는 경우는 없고
# 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
# 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.
def shark_move():
    temp = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if board[i][j]:
                r, c, s, d, z = i, j, board[i][j][0], board[i][j][1], board[i][j][2]
                while s > 0:
                    r += dy[d]
                    c += dx[d]
                    if 1 <= r < R + 1 and 1 <= c < C + 1:
                        s -= 1
                    else:
                        r -= dy[d]
                        c -= dx[d]
                        if not d:
                            d = 1
                        elif d == 1:
                            d = 0
                        elif d == 2:
                            d = 3
                        elif d == 3:
                            d = 2
                if not temp[r][c]:
                    temp[r][c] = [board[i][j][0], d, z]
                else:
                    if temp[r][c][2] < z:
                        temp[r][c] = [board[i][j][0], d, z]
    return temp


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
R, C, M = map(int, input().split())
# 2 ≤ R, C ≤ 100
board = [[0] * (C + 1) for _ in range(R + 1)]
answer = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다.
    board[r][c] = [s, d - 1, z]
for i in range(1, C + 1):  # 무조건 최대 100번 탐색
    for j in range(1, R + 1):  # 최대 100번 탐색하지만 중간에 중지할 수도 있음.
        if board[j][i]:
            answer += board[j][i][2]
            board[j][i] = 0
            break
    board = shark_move()  # 상어의 위치를 일일히 찾을 경우 최대 100 * 100번 탐색.
print(answer)
