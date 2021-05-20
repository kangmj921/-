# 출발 하는 위치에서부터 다이나믹 프로그래밍을 진행한다.
# 선택할 수 있는 항의 값의 합이 곧 총 경로의 개수이다.
# 이렇게 진행하였을때, 도착해야 하는 위치에서 기록되는 값이 곧
# 총 경로의 개수이다.
N = int(input())
game_board = []
for _ in range(N):
    game_board.append(list(map(int, input().split())))
dp_list = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
