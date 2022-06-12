# 각 방향으로 이동할 확률을 어떻게 구현해야 할지 고민이다.
# 입력 받은 확률 자연수의 횟수대로 이동경로를 브루트포스 하면 당연히 시간초과가 날 것이다.
# 로봇이 같은 곳을 아예 이동하지 않을 확률이 단순할 확률일 것이다.
# 처음 로봇이 있는 위치를 N, N이라 했을 때, 로봇이 최대 이동할 수 있는 거리가 N이므로 전체 그래프의
# 크기는 2N + 1 * 2N + 1으로 놓는다.
# 이 그래프를 기준으로 방문한 곳을 지나지 않는 경로를 구해본다.
# 각 경로를 지날 때마다 확률을 곱해주면 결국 총 경로의 확률을 구할 수 있다.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(c, index, p):
    global answer
    if c == N:
        # print(board_list)
        answer += p
        return
    for i in range(4):
        ny = index[0] + dy[i]
        nx = index[1] + dx[i]
        if not board_list[ny][nx]:
            board_list[ny][nx] = 1
            DFS(c + 1, (ny, nx), p * p_list[i])
            board_list[ny][nx] = 0


answer = 0
N, Me_p, Mw_p, Ms_p, Mn_p = map(int, input().split())
p_list = [Me_p / 100, Mw_p / 100, Ms_p / 100, Mn_p / 100]
board_list = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
board_list[N][N] = 1
DFS(0, (N, N), 1)
print("{}".format(answer))
