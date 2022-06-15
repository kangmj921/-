# 초기  주사위를 배열로 나타내게 되면,
# [[0, 0] [2, 0] [0, 0]]
# [[4, 0] [1, 0] [3, 0]]
# [[0, 0] [5, 0] [0, 0]]
# [[0, 0] [6, 0] [0, 0]]
# 남과 북 방향으로 주사위가 이동할때는 초기 배열 기준, 4, 3 번호가 붙은 면은 위치가 변하지 않고
# 동과 서 방향으로 주사위가 이동할때는 초기 배열 기준, 2, 5 번호가 붙은 면은 위치가 변하지 않는다.
# 남 북 그리고 동 서 방향으로 주사위가 이동할 때 면이 바뀌는 규칙에 따라 바꿔준다.

# 문제에 전개도가 왜 있나 했더니, 주사위의 상태를 어떻게 나타낼지에 대한 힌트였다.
# 생각하는데 시간이 걸렸지만, 잘 풀어서 다행이다.

def check_dice_up_front(c):  # 주사위 상단의 수 반환.
    if c == 1:
        a, b, c, d = initial_dice[3], initial_dice[4], initial_dice[5], initial_dice[10]
        initial_dice[3], initial_dice[4], initial_dice[5], initial_dice[10] = b, c, d, a
    elif c == 2:
        a, b, c, d = initial_dice[3], initial_dice[4], initial_dice[5], initial_dice[10]
        initial_dice[3], initial_dice[4], initial_dice[5], initial_dice[10] = d, a, b, c
    elif c == 3:
        a, b, c, d = initial_dice[1], initial_dice[4], initial_dice[7], initial_dice[10]
        initial_dice[1], initial_dice[4], initial_dice[7], initial_dice[10] = d, a, b, c
    else:
        a, b, c, d = initial_dice[1], initial_dice[4], initial_dice[7], initial_dice[10]
        initial_dice[1], initial_dice[4], initial_dice[7], initial_dice[10] = b, c, d, a
    return initial_dice[10][1]


# E : 1, W : 2, N : 3, S : 4
N, M, y, x, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
command_list = list(map(int, input().split()))
dx = [None, 1, -1, 0, 0]
dy = [None, 0, 0, -1, 1]
initial_dice = [[0, 0], [2, 0], [0, 0],  # 초기 주사위의 상태, 각 리스트는 [주사위의 면 index, 해당 면의 값]
                [4, 0], [1, 0], [3, 0],
                [0, 0], [5, 0], [0, 0],
                [0, 0], [6, 0], [0, 0]]
initial = 1
for i in command_list:
    # print(i, 'result : ', end=" ")
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
    result = check_dice_up_front(i)
    if initial_dice[4][1] and not map_list[ny][nx]:  # 바닥면에 쓰인 수가 0이 아니고, 이동한 칸에 쓰여있는
        # 수가 0일때, 주사위의 바닥면에 쓰인 수가 칸에 복사됨.
        map_list[ny][nx] = initial_dice[4][1]
    elif map_list[ny][nx]:  # 0이 아닌 경우, 칸에 쓰인 수가 주사위의 바닥면에 복사됨.
        initial_dice[4][1] = map_list[ny][nx]
        map_list[ny][nx] = 0
    y, x = ny, nx
    print(result)
