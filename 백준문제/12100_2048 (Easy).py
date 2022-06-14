#  처음엔 각 수를 옮기는 방법을 0이 아닌 수를 만나면, 스택에 넣고 나중에 넣은 것이
#  먼저 나오니까, 오른쪽으로 이동하는 거면, 제일 왼쪽거를 먼저 넣고 오른쪽 것을 나중에 넣는 식으로
#  했는데, 이 과정에서 계속 틀려서 오답이 나온 것 같다.
#  간단하게 index를 이용해서 구할 수 있었다.
import copy


def move(b, d):
    if d == 0:  # 오른쪽으로 이동
        for i in range(N):  # 0, 1 - > 0, 2 -> 0, 3
            right = N - 1
            for j in range(N - 2, -1, -1):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if not b[i][right]:
                        b[i][right] = temp
                    elif b[i][right] == temp:
                        b[i][right] = temp * 2
                        right -= 1
                    else:
                        right -= 1
                        b[i][right] = temp
    elif d == 1:  # 왼쪽으로
        for i in range(N):
            left = 0
            for j in range(1, N):
                if b[i][j]:
                    temp = b[i][j]
                    b[i][j] = 0
                    if not b[i][left]:
                        b[i][left] = temp
                    elif b[i][left] == temp:
                        b[i][left] = temp * 2
                        left += 1
                    else:
                        left += 1
                        b[i][left] = temp
    elif d == 2:  # 위쪽으로   3,0 2,0 1,0
        for i in range(N):
            top = 0
            for j in range(1, N):
                if b[j][i]:
                    temp = b[j][i]
                    b[j][i] = 0
                    if not b[top][i]:
                        b[top][i] = temp
                    elif b[top][i] == temp:
                        b[top][i] = temp * 2
                        top += 1
                    else:
                        top += 1
                        b[top][i] = temp
    else:  # 아래쪽으로  0, 0 1, 0
        for i in range(N):
            down = N - 1
            for j in range(N - 2, -1, -1):
                if b[j][i]:
                    temp = b[j][i]
                    b[j][i] = 0
                    if not b[down][i]:
                        b[down][i] = temp
                    elif b[down][i] == temp:
                        b[down][i] = temp * 2
                        down -= 1
                    else:
                        down -= 1
                        b[down][i] = temp
    return b


def dfs(board, cnt):
    global answer
    if cnt == 5:
        for row in range(N):
            for col in range(N):
                answer = max(answer, board[row][col])
        return
    for i in range(4):
        c = move(copy.deepcopy(board), i)
        dfs(c, cnt + 1)


N = int(input())
answer = 0
board_list = [list(map(int, input().split())) for _ in range(N)]
dfs(board_list, 0)
print(answer)
