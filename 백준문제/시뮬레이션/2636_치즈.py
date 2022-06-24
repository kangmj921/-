from collections import deque


def bfs_search(y, x):
    queue = deque()
    queue.append((y, x))
    visit_list[y][x] = True
    result_list = []
    while queue:
        y, x = queue.popleft()
        if board_list[y][x]:
            visit_list[y][x] = True
            result_list.append((y, x))
        else:
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= R or nx >= C:
                    continue
                if not visit_list[ny][nx]:
                    visit_list[ny][nx] = True
                    queue.append((ny, nx))
    return result_list


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
R, C = map(int, input().split())
board_list = [list(map(int, input().split())) for _ in range(R)]
visit_list = [[False] * C for _ in range(R)]
time = 0
answer_list = []
while True:
    if not time:
        result_list_1 = deque(bfs_search(0, 0))
    else:
        temp = []
        length = len(result_list_1)
        answer_list.append(length)
        for i in range(length):
            y, x = result_list_1.popleft()
            board_list[y][x] = 0
            temp = bfs_search(y, x)
            for i in range(len(temp)):
                result_list_1.append(temp[i])
        if not result_list_1:
            break
    time += 1
print(time)
print(answer_list[-1])
