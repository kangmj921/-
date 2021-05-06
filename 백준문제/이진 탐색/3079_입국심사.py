# 이진 탐색을 응용하여 푸는 문제인데, 이런 문제도 이진 탐색을
# 활용할 수 있다는 것을 알게 되었다. 이진 탐색을 이용하는 문제를
# 더 많이 풀어봐야 할 것 같다.
# 경우에 따른 최소 소요 시간과 최대 소요 시간을 정하고,중간의 소요 시간까지
# 총 몇 명을 검사할 수 있는지 체크 하고,
# 체크한 인원수가 M보다 작다면, 중간 소요 시간의 값을 늘리기 위해
# 최소 소요 시간을 조정하고, 많거나 같다면 최대 소요시간을 조정하고
# 최종적으로 최소 소요 시간을 출력하도록 하였다.
# 파이썬으로 제출하면 시간초과가 난다. pypy3은 문제가 없는데..
# 검사 받은 인원 수를 구하는 과정에서 time_list의 모든 원소를 확인
# 하는 과정 때문인데, 앞서서 풀어본 문제에서 겪은 문제와 동일한 문제로,
# list comprehension을 이용하니 해결할 수 있었다.
import sys


N, M = map(int, input().split())
time_list = [int(sys.stdin.readline()) for _ in range(N)]
min_t, max_t = min(time_list), max(time_list) * M
while min_t <= max_t:
    checked = 0
    mid_t = (min_t + max_t) // 2
    # for i in time_list:
    #     checked += mid_t // i     # python3에서는 시간초과됨.
    checked = sum([mid_t // i for i in time_list])
    if checked < M:
        min_t = mid_t + 1
    else:
        max_t = mid_t - 1
print(min_t)
