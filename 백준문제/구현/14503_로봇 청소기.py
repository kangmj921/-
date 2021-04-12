def turn_left(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction


N, M = map(int, input().split())
y, x, d = map(int, input().split())
direction_list = {
    0: (0, -1),  # north
    1: (1, 0),  # east
    2: (0, 1),  # south
    3: (-1, 0)  # west
}
state_status = []
cleaned = 0
rotate_count = 0
for i in range(N):
    state_status.append(list(map(int, input().split())))
while True:
    if state_status[y][x] == 0:
        state_status[y][x] = 10
        cleaned += 1
    d = turn_left(d)
    rotate_count += 1
    ny = y + direction_list[d][1]
    nx = x + direction_list[d][0]
    if state_status[ny][nx] == 0:
        x, y = nx, ny
        rotate_count = 0
        continue
    if rotate_count >= 4:
        py = y - direction_list[d][1]
        px = x - direction_list[d][0]
        if state_status[py][px] == 1:
            break
        else:
            x, y = px, py
            rotate_count = 0
print(cleaned)
