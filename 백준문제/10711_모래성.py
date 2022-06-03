#  모래성의 최대 크기는 998 * 998이다. 매 회마다 2차원 리스트의 각 원소를 8회 탐색하게 되면
#  시간 제한에 걸릴 수 있는 가능성이 있다.
# dp는 구현 방법이 복잡한 것 같고, 맞는 값으로 저장하는게 아닌거 같아서 다른 방법으로 해본다.
# queue에 9나 .이 아니고, 8이하인 경우, 주변에 9의 개수를 뺀 격자의 개수가 강도와 같거나 작은 경우
# stack에 좌표를 넣는다. stack의 모든 좌표에 해당하는 곳을 .으로 바꾸는걸 반복시켰는데
# 시간초과에 걸림.
# from collections import deque
#
#
# def check_8_dir(y, x, a, n):
#     count = 0
#     for i in range(8):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if n == 0:
#             if sand_castle[ny][nx] == '.' or sand_castle[ny][nx] != '9':
#                 count += 1
#         else:
#             if sand_castle[ny][nx] == '.':
#                 count += 1
#     if count >= a:
#         return True
#     return False
#
#
# H, W = map(int, input().split())
# answer = 0
# stack = []
# sand_castle = []
# queue1 = deque()
# queue2 = deque()
# dx = [-1, 1, 0, 0, 1, 1, -1, -1]
# dy = [0, 0, -1, 1, -1, 1, -1, 1]
# for i in range(H):
#     sand_castle.append(list(input().rstrip()))
# for i in range(H):
#     for j in range(W):
#         if sand_castle[i][j] != '.' and sand_castle[i][j] != '9':
#             if check_8_dir(i, j, int(sand_castle[i][j]), 0):
#                 queue1.append((i, j, int(sand_castle[i][j])))
# check = False
# while not check:
#     while queue1:
#         y, x, g = queue1.popleft()
#         c = 0
#         if check_8_dir(y, x, g, 1):
#             stack.append((y, x))
#         else:
#             queue2.append((y, x, g))
#     if len(stack) > 0:
#         for i in range(len(stack)):
#             y, x = stack.pop()
#             sand_castle[y][x] = '.'
#         answer += 1
#     else:
#         check = True
#     while queue2:
#         queue1.append(queue2.popleft())
# print(answer)


# 다른 방법으로, 매번 주위 8개의 격자를 확인하게 되면 시간초과에 걸리는 거 같다.
# 처음 실행시 모든 리스트를 돌면서 .인 곳에 대해 queue에 저장하고 queue를 돌면서
# 숫자가 있는 곳에 들리게 되면 강도를 1씩 뺀다. 0인 곳이 곧 .인 곳이다. 그리고 queue에 넣는다.
# 이 과정을 반복한다.
from collections import deque
import sys


H, W = map(int, input().split())
visited = [[0] * W for _ in range(H)]
answer = 0
sand_castle = [list(sys.stdin.readline()) for _ in range(H)]
queue = deque()
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
for i in range(H):
    for j in range(W):
        if sand_castle[i][j] == '.':
            sand_castle[i][j] = 0
            queue.append((i, j))
        else:
            sand_castle[i][j] = int(sand_castle[i][j])
while queue:
    y, x = queue.popleft()
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 > nx or nx >= W or 0 > ny or ny >= H:
            continue
        if sand_castle[ny][nx] != 0:
            sand_castle[ny][nx] -= 1
            if sand_castle[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                answer = max(answer, visited[ny][nx])
                queue.append((ny, nx))
print(answer)
