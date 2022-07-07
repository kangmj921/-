# python3 로는 시간초과에 걸리고, pypy3로는 걸리지 않았다.
# 탐색과정에서 줄일 수 있는게 있다면 줄여야겠다.

# 처음엔 빈칸이 있는지 아닌지 확인하는 과정을 모든 리스트를 돌면서 확인하였는데,
# 이 과정을 처음에 빈 칸의 개수를 세어 놓고, 바이러스가 퍼지는 과정에서 걸리는 시간을 구하는 과정에서
# 퍼진 칸 들을 세고 이 두 수가 같다면 빈 곳이 없다는 뜻이므로, 탐색을 하지 않고도
# 빈 칸이 있는지 없는지 확인하는 과정으로 수정하였다.
# 그래도 시간초과가 걸리기에, visit 를 매 조합의 경우의 수마다 만들지 않도록 해줘도 걸렸다.

# python3로 통과한 사람들의 코드를 살펴보니, 공통적으로, 바이러스가 조합이 어떻게 되든,
# 각 케이스에 바이러스들의 BFS 결과는 항상 같기 때문에, 미리 모든 바이러스에 대해
# BFS 결과를 저장해 놓고, 각 조합에서 고른 바이러스 들의 BFS 결과들을 합쳐서 계산을 했다.
#
# 그런데 처음 내가 푼 방식이랑 비슷하게 푼 사람이 있었는데 이 사람은 시간 초과를 통과했다.
# 그 이유를 보니, 나는 단순히 반복문안에 BFS 부분을 바로 넣었지만, 이 사람은 함수로 BFS 부눈을
# 따로 빼놓고 구현을 했다.
# 함수로 반복문
import sys
from collections import deque


def combination_by_m(idx, l):
    if len(l) == M:
        virus_location.append(l[:])
        return
    for i in range(idx, len(temp)):
        combination_by_m(i + 1, l + [temp[i]])


def bfs(v_list, r):  # 최대 O(V + E) = O(2500) * O(2500)
    visit = [[-1] * N for _ in range(N)]
    queue = deque()
    for pos in v_list:
        queue.append(pos)
        visit[pos[0]][pos[1]] = 0
    cnt = 0
    count = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or lab[ny][nx] == 1 or visit[ny][nx] != -1:
                continue
            visit[ny][nx] = visit[y][x] + 1
            if not lab[ny][nx]:
                cnt = max(cnt, visit[ny][nx])
                count += 1
            queue.append((ny, nx))
    if count == r:
        answer.append(cnt)


visit_dict = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, sys.stdin.readline().split())
# N(4 ≤ N ≤ 50), M(1 ≤ M ≤ 10)
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치
temp, virus_location = [], []
answer = []
result = 0
for i in range(N):
    for j in range(N):
        if not lab[i][j]:
            result += 1
        if lab[i][j] == 2:
            temp.append((i, j))  # M보다 크거나 같고 10보다 작거나 같음.
# 모든 바이러스를 놓을 수 있는 위치 중 M개의 조합을 찾아서 계산하면
# 10CM 개의 경우를 얻을 수 있다. 이 경우 최대 10C5 = 252, O(V + E) = O(2500) * O(2500)
#
combination_by_m(0, [])
for v_m in virus_location:  # 최대 252번.
    bfs(v_m, result)  # bfs를 함수로 빼면 시간초과가 안걸린다?
print(min(answer) if answer else -1)
