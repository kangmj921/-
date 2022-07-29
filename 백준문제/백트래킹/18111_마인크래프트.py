
# 1 ≤ M, N ≤ 500, 0 ≤ B ≤ 64,000,000
# 땅의 블록을 캐내 인벤에 넣는 과정의 시간이 1초이고 인벤에서 빼서 채우는건 2초이다.
# 따라서 다른 땅의 블록을 캐서 다른 땅에 채우는 방식이 드는 시간은 총 3초,
# 그냥 인벤에 있던 블록을 채우는 건 2초이다. 최소 시간을 구하기 위해
# 최대한 인벤에 있는 블록을 사용하는데, 다 써서 없을 경우에만 캐내 인벤에 넣는다.
# 다 써서 없을 땐, 우선적으로 제일 높은 블록에서 캐와서 제일 낮은 곳에 채워 넣어야한다.
# 이러러면 제일 높은 높이와 낮은 높이인 곳을 찾아야 하는데,
# 일일히 찾고 캐서 채우는 방식은 매회 탐색하는 횟수가 최대 500 * 500이므로 시간 초과의 위험이 있다.

# 따라서 더 간단하고 시간 복잡도가 높지 않은 방식을 생각하다가 높이의 값에 따른 시간을 구하는 방식이
# 생각났다. 블록의 높이가 0~256 으로 정해져 있으므로, 0 부터 256 까지 i 값의 루프를 돌리면서
# 모든 판의 높이를 i 값으로 맞추는데 필요한 시간을 구하고 최소 시간을 구할 것이다.
# 시간을 구하는 기준은 i * 판의 크기가 필요한 블록의 수인데, i 보다 커서 남는 블록들의 수 + 인벤토리의
# 블록 수가 필요한 총 블록의 수 보다 같거나 클 때 해당 i 값으로 평탄화 할 수 있다.
# 만약 중간에 할 수 없다면 그 이상의 i 값은 진행 불가하므로 탐색을 중지시킨다.
# 조건에 답이 여러 개라면 땅의 높이가 높은 것이 있었다...
import math
import sys


def check_height(h, b):
    remained_block, time = b, 0
    for i in range(N):  # 최대 500
        for j in range(M):  # 최대 500
            diff = ground_list[i][j] - height
            if diff >= 0:
                remained_block += diff
                time += 2 * diff
            else:
                remained_block -= abs(diff)
                time += abs(diff)
    if remained_block >= 0:
        return time
    else:
        return math.inf


N, M, B = map(int, input().split())
# N * M의 크기의 격자판에 B는 가지고 있는 블록 개수.
ground_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer_time = math.inf
answer_height = 0
for height in range(257):  # 최대 256번 시행
    temp = check_height(height, B)
    if answer_time > temp:
        answer_time = temp
        answer_height = height
    elif answer_time == temp:
        answer_height = max(answer_height, height)
    if temp == math.inf:
        break
print(answer_time, answer_height)
