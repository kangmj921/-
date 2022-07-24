def move_marker(n, y, x, d, ny, nx, color):  # n 번째 말 이동시키는 함수.
    global game_end
    start, end = marker_index[n], len(visit_list[y][x])
    if not color:  # FIFO
        for i in range(start, end):
            temp = visit_list[y][x][i]
            visit_list[ny][nx].append(temp)
            marker_index[temp] = len(visit_list[ny][nx]) - 1
            marker_list[temp] = [ny, nx, marker_list[temp][2]]
        for _ in range(start, end):
            visit_list[y][x].pop()
    else:  # FILO
        for i in range(end - 1, start - 1, -1):
            temp = visit_list[y][x][i]
            visit_list[ny][nx].append(temp)
            marker_index[temp] = len(visit_list[ny][nx]) - 1
            marker_list[temp] = [ny, nx, marker_list[temp][2]]
        for _ in range(end - 1, start - 1, -1):
            visit_list[y][x].pop()
    if len(visit_list[ny][nx]) >= 4:
        game_end = True


marker_index = {}
N, K = map(int, input().split())
# 4 ≤ N ≤ 12, 4 ≤ K ≤ 10
board = [list(map(int, input().split())) for _ in range(N)]
marker_list = [[0]]
# 말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다.
# 행과 열의 번호는 1부터 시작하고, 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.
direction = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
visit_list = [[[] for _ in range(N)] for _ in range(N)]
for i in range(1, K + 1):
    y, x, d = map(int, input().split())
    marker_list.append([y - 1, x - 1, d])
    visit_list[y - 1][x - 1].append(i)
    marker_index[i] = len(visit_list[y - 1][x - 1]) - 1
# marker_index 엔 말이 어느 높이에 높여있는지 저장, visit_list 엔 각 인덱스에 어떤 말이 있는지 저장.
turn = 0
game_end = False
while turn < 1000:
    turn += 1
    for i in range(1, K + 1):  # 최대 K 번
        y, x, d = marker_list[i]
        # marker_list 엔 i번째 말의 정보가 저장되어있음, 좌표라던지 이동방향이라던지.
        ny, nx = y + direction[d][0], x + direction[d][1]
        if (0 <= ny < N and 0 <= nx < N) and (board[ny][nx] == 1 or not board[ny][nx]):
            move_marker(i, y, x, d, ny, nx, board[ny][nx])
        else:
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            else: d = 3
            ny, nx = y + direction[d][0], x + direction[d][1]
            if 0 <= ny < N and 0 <= nx < N and (board[ny][nx] == 1 or not board[ny][nx]):
                move_marker(i, y, x, d, ny, nx, board[ny][nx])
            else:
                ny, nx = y, x
            marker_list[i] = [ny, nx, d]
        if game_end:
            print(turn)
            exit()
print(-1)
