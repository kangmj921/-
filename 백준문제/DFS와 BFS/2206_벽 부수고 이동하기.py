# N * M 이 1,000,000 이므로 까딱 잘못하면 시간초과가 날 수 있다.
# 1이 있는 곳 하나 마다 뽑아서 0으로 만드는 브루트포스 식으로 하면,
# 최악의 경우 : 맵의 1 하나씩 뽑아 0으로 만들고 BFS로 최단거리구함 = 1,000,000 * O(1,000,000)
# 이므로 시간복잡도를 줄일 필요가 있다. 따라서 1을 하나씩 뽑아 0으로 만드는 과정의
# 수를 줄이는 수밖에 없을 것 같다. 1을 뽑되, 주위가 1로 둘러쌓여 갇히거나 접근할 수 없는 경우는 제외해서
# 진행해보려고 한다. 일단 간단하게 상하좌우에 0이 없는 1은 제외하고 결과를 봐야할것같다.
# 시간초과가 난다. 더 경우의 수를 줄이든지 접근 방법을 바꿔야 할 것 같다..
# 더 경우의 수를 줄이려면 주위에 최소 0이 2개는 되야 할 것 같다. 그래야 이동경로 상 막고 있는
# 벽일 경우가 높다. 그래도 시간초과가 걸린다. 접근 방식을 바꿔야 할 것 같다.
# 탐색을 하는 동안 벽을 세울 수 있도록 해야할 것 같다.
# 이제부터 최단거리는 visited 를 이용해서 구하면 될 것같다.
# visited를 3차원 리스트로 구현해서 벽을 이미 세웠을 때랑 아닐 때랑 구분해서 기록하는 방식
# 으로 해야 될 것 같다. 이 방법으로 하니까 해결 되었다.
from collections import deque


N, M = map(int, input().split())
maze_map = []
for i in range(N):
    maze_map.append(list(map(int, input().rstrip('\n'))))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
check_arrived = False
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
while queue:
    y, x, wall_count = queue.popleft()
    if (y, x) == (N-1, M-1):
        check_arrived = True
        print(visited[wall_count][N-1][M-1])
        exit()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if maze_map[ny][nx] == 1 and wall_count == 0:
            visited[wall_count + 1][ny][nx] = visited[wall_count][y][x] + 1
            queue.append((ny, nx, 1))
        if maze_map[ny][nx] == 0 and visited[wall_count][ny][nx] == 0:
            visited[wall_count][ny][nx] = visited[wall_count][y][x] + 1
            queue.append((ny, nx, wall_count))
if not check_arrived:
    print(-1)
