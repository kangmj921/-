import sys

# 게임판에 대한 이해를 잘못해서 입력받은 판 주위에 벽을 치는 작업을 따로 수행한 것 때문에
# 답을 구하는데 어려움을 겪었다. 지문을 잘 이해하는 것이 필요할 거 같다.


def turn(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction


def solution(g, d):
    d_index = 0
    x, y = 1, 1
    t_p = [(x, y)]
    curr_time = 0
    direction = 0
    curr_dict = {
        0: (0, 1),  # east
        1: (1, 0),  # south
        2: (0, -1),  # west
        3: (-1, 0)  # north
    }
    while True:
        nx = x + curr_dict[direction][0]
        ny = y + curr_dict[direction][1]
        if 1 <= nx <= N and 1 <= ny <= N and game_board[nx][ny] != 2:
            if game_board[nx][ny] == 0:
                t_p.append((nx, ny))
                game_board[nx][ny] = 2
                px, py = t_p.pop(0)
                game_board[px][py] = 0
            if game_board[nx][ny] == 10:
                game_board[nx][ny] = 2
                t_p.append((nx, ny))
        else:
            curr_time += 1
            break
        x, y = nx, ny
        curr_time += 1
        if d_index < len(d) and curr_time == int(d[d_index][0]):
            direction = turn(direction, d[d_index][1])
            d_index += 1
        #print((x, y), t_p, curr_time, direction)
    return curr_time


N = int(input())
game_board = [[0] * (N + 1) for i in range(N + 1)]
game_board[1][1] = 2
d_t = []
K = int(input())
for i in range(K):
    a, b = map(int, sys.stdin.readline().split())
    game_board[a][b] = 10
L = int(input())
for i in range(L):
    d_t.append(list(sys.stdin.readline().split()))
print(solution(game_board, d_t))
