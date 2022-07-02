from collections import deque
import math


dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
N, M, K = map(int, input().split())  # N은 땅의 크기, M은 나무의 수, K는 구할 K년 후
# N <= 10, M <= N ^ 2, K <= 1000


# 봄에는
# (r, c)에 심어진 나무들은 나이가 적은 순으로 자신의 나이만큼 양분을 소비하고, 나이 1 먹는다.
# 만약 양분이 자신의 나이보다 없다면 바로 죽는다.
def year_by_year(t, year):
    global answer
    bunsik = []
    d_t_list = []
    while t:
        y, x = t.popleft()
        temp = len(tree_list[y][x])
        for _ in range(temp):
            tree_age = tree_list[y][x].popleft()
            if ground[y][x] < tree_age:  # 여름에는 죽은 나무가 있다면, 죽은 나무의 나이를 2로 나눈 값이
                d_t_list.append([y, x, tree_age])  # 나무가 있던 자리에 양분으로 추가된다.
            else:
                ground[y][x] -= tree_age
                tree_list[y][x].append(tree_age + 1)
                if (tree_age + 1) % 5 == 0:
                    bunsik.append([y, x])
    for y, x, z in d_t_list:
        ground[y][x] += math.floor(z / 2)
    bunsik = deque(bunsik)
    while bunsik:
        y, x = bunsik.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if not tree_list[ny][nx]:
                tree_list[ny][nx] = deque([1])
            else:
                tree_list[ny][nx].appendleft(1)
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]
            if tree_list[i][j]:
                t.append([i, j])
                if year == K:
                    answer += len(tree_list[i][j])


# k년후 살아있는 나무의 개수를 구하는 프로그램.
answer = 0
A = []
ground = [[5] * N for _ in range(N)]
tree_list = [[list()] * N for _ in range(N)]
t_list = deque()
for _ in range(N):  # 겨울마다 S2D2가 추가할 양분 리스트
    A.append(list(map(int, input().split())))
for _ in range(M):
    y, x, z = map(int, input().split())
    if not tree_list[y - 1][x - 1]:
        tree_list[y - 1][x - 1] = [z]
    else:
        tree_list[y - 1][x - 1].append(z)
for i in range(N):
    for j in range(N):
        if tree_list[i][j]:
            tree_list[i][j].sort()
            tree_list[i][j] = deque(tree_list[i][j])
            t_list.append([i, j])
year = 1
while year <= K:
    year_by_year(t_list, year)
    year += 1
print(answer)
