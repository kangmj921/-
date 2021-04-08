import sys


def turn_left():
    global c
    c -= 1
    if c == -1:
        c = 3


N, M = map(int, input().split())
a, b, c = map(int, input().split())
game_map = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
visited = [[0] * M for i in range(N)]
visited[a][b] = 1
result, turn_time = 1, 0
direction = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0)
}
while True:
    turn_left()
    next_row = a + direction[c][0]
    next_column = b + direction[c][1]
    if visited[next_row][next_column] == 0 and game_map[next_row][next_column] == 0:
        a, b = next_row, next_column
        visited[a][b] = 1
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        next_row = a - direction[c][0]
        next_column = b - direction[c][1]
        if game_map[next_row][next_column] == 0:
            a = next_row
            b = next_column
        else:
            break
        turn_time = 0
print(result)
