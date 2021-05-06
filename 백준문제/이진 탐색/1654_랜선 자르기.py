# 앞서서 풀었던 떡볶이 떡 만들기 문제와 비슷한 방식으로 풀 수 있었다.
# 하지만, 자른 개수가 N보다 큰 경우도 N개를 만드는 것에 포함시킨 것이
# 다른 점이 었다. 만약 전에 풀었던 문제와 똑같이 N보다 큰 경우와 딱 N으로
# 맞아 떨어지는 경우를 나눠서 탐색하게 되면 시간 초과가 나는 것을 알 수 있었다.
import sys


K, N = map(int, input().split())
cable_list = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(cable_list)
while start <= end:
    result = 0
    mid = abs(start + end) // 2
    for i in cable_list:
        result += (i // mid)
    if result < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)
