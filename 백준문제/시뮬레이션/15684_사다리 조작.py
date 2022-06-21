# 추가 가능한 가로선 목록을 구현하는데 시간이 많이 걸렸다.
# 평소에 조합을 직접 구현해 봤으면, 금방 구현이 가능했을 것이다.

# 답안을 내보니, 메모리 초과가 걸렸다.
# 시간초과나 메모리 초과를 통과하기 위해선, 가로선의 조합을 구한 쪽을 건드려야 할 것 같다.
# 확인해보니 조합을 생성할때, 원소가 중복되는 경우가 있었다.
# 직접 조합을 구현하기 어려워 결국 combination을 썻다.

# 직접 조합을 구하니 시간 초과를 통과하기가 어려웠다. 다른 사람이 푼 걸 보니
# 조합으로도 시간이 넉넉하게 통과된 사람들이 있었다. 백트래킹을 더 해봐야겠다
# 사다리를 놓을 수 있는 곳을 선택할 때, 오른쪽에 있는 거만 고려하기로 했다.
# 어짜피 왼쪽에서 오른쪽으로 가면서 어디에 놓을지 정하는 거니까 현재 위치와 그 다음 위치에
# 사다리가 존재하지 않으면 선택한다.
# 그리고 탐색할 리스트의 길이를 줄이기로 하였다. 기존에는 세로선도 포함해서 리스트를 만들었지만,
# 이제는 그냥 사다리의 상태만 나타내는 리스트로 다시 만들어 가로 길이를 반으로 줄였다.

# 그리고 사다리의 왼쪽 오른쪽을 구별해주기 위해, 사다리의 왼쪽과 연결된 곳은 1로
# 오른쪽은 -1로 초기화해서, 세로선에서 탐색하는 중에, -1를 먼저 만나면 왼쪽으로,
# 1을 먼저 만나면 오른쪽으로 갈 수 있게 해주었다.
# 그리고 함수 호출이 많을 수록 시간이 느려진다는 것도 알았다.
# pypy3로 냇을때는 확실히 빨라졌지만 아직도 python3 에선 시간초과였다.
# 잘 살펴보니, i번 세로선이 i 번으로 도착하지 않는 경우가 6개 보다 크면,
# 최대 3개의 가로선을 놓아도 조건을 만족할 수 없기 때문에
# 탐색 전에 이 경우는 백트래킹을 해줘야했다.

# 코드의 효율성엔 백트래킹도 매우 큰 부분을 차지한다는 것을 알게 되었다....
# 특히 완전탬색 문제의 경우 더 신경써줘야겠다.
from itertools import combinations
import math
import sys


# 모든 세로선에 대해 같은 세로선으로 갈 수 있는지 출발해봄.
def check_ladder():  # 최대 N * H번 탐색함.
    result = 0
    for start in range(N):
        row = 0
        col = start
        while row < H:
            if ladder[row][col] == 1:
                col += 1
            elif ladder[row][col] == -1:
                col -= 1
            row += 1
        if col != start:
            result += 1
    return result


N, M, H = map(int, sys.stdin.readline().split())  # N은 최대 10, H는 최대 30
ladder = [[0] * N for _ in range(H)]
check = False
# ladder 리스트의 최대 사이즈는 19 * 30 = 570
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    ladder[a - 1][b - 1] = 1
    ladder[a - 1][b] = -1
add_line = []
answer = math.inf
check = False
for i in range(H):
    for j in range(N - 1):
        if not ladder[i][j] and not ladder[i][j + 1]:
            add_line.append((i, j))
if check_ladder() > 6:
    print(-1)
    exit()
for add_num in range(4):  # 추가할 가로선을 0개부터 시작해서 조건을 만족하는지 봄.
    for add_ladder in combinations(add_line, add_num):
        for y, x in add_ladder:
            if ladder[y][x]:
                break
            ladder[y][x] = 1
            ladder[y][x + 1] = -1
        if not check_ladder():
            answer = add_num
            check = True
            break
        else:
            for y, x in add_ladder:
                ladder[y][x] = 0
                ladder[y][x + 1] = 0
    if check:
        break
if answer != math.inf:
    print(answer)
else:
    print(-1)
