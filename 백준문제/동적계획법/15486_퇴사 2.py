# 퇴사1 문제에서 N의 범위만 늘어난 문제.
# dp로 해결하지 않는다면 시간 제한에 걸릴듯.
import sys


N = int(input())
pay = []
day = []
dp_list = [0] * (N + 1)
max_value = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    pay.append(b)
    day.append(a)
for i in range(N - 1, -1, -1):
    if day[i] + i > N:
        dp_list[i] = max_value
    else:
        dp_list[i] = max(max_value, dp_list[i + day[i]] + pay[i])
        max_value = dp_list[i]
print(dp_list[0])
