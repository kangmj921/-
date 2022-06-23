# 처음엔 단순하게 모든 방을 출발로 해서 BFS로 했는데, 최악 시간복잡도가 N * N * N * N으로
# 10 ^ 12가 나와서 제한 시간에 걸렸다.
# 그래서 dp를 쓰기로 했다. dp의 각 인덱스는 해당 인덱스에서 출발할때 갈 수 있는 최대 방 수
# dp 인덱스의 값이 존재하지 않을 때,주위에 값이 저장되어 있고, 방 번호가 1 작은 인덱스를 찾는다.
# 있다면 해당 dp 인덱스의 값은 찾은 인덱스의 값 - 1, 없으면 bfs 돌려서 저장한다.
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_search(y, x):
    visit = [[False] * N for _ in range(N)]
    res = 0
    queue = deque()
    queue.append((y, x, 1))
    while queue:
        y, x, cnt = queue.popleft()
        visit[y][x] = True
        res = max(cnt, res)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if not visit[ny][nx] and A_list[y][x] + 1 == A_list[ny][nx]:
                queue.append((ny, nx, cnt + 1))
    return res


for T in range(int(input())):
    N = int(input())
    A_list = [list(map(int, input().split())) for _ in range(N)]
    dp_list = [[0] * N for _ in range(N)]
    answer = -1
    min_a = 10 ** 9
    for i in range(N):
        for j in range(N):
            if not dp_list[i][j]:
                check = False
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]
                    if ni < 0 or nj < 0 or ni >= N or nj >= N:
                        continue
                    if dp_list[ni][nj] and A_list[ni][nj] + 1 == A_list[i][j]:
                        dp_list[i][j] = dp_list[ni][nj] - 1
                        check = True
                if not check:
                    dp_list[i][j] = bfs_search(i, j)
    for i in range(N):
        for j in range(N):
            if dp_list[i][j] > answer:
                answer = dp_list[i][j]
                min_a = A_list[i][j]
            elif dp_list[i][j] == answer:
                if A_list[i][j] < min_a:
                    min_a = A_list[i][j]
    print("#{} {} {}".format(T + 1, min_a, answer))
