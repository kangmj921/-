# 전체 용액의 수가 1000,000이 최대이므로 리스트를 하나씩 돌며 한 원소를 고르고
# 나머지 원소는 이진탐색으로 합이 0에 가까울 수 있는 원소를 고름으로서
# 시간복잡도가 O(N*N)이 아닌 O(N*logN)이 될 수 있도록 하였다.
# 합의 절댓값이 작아질수록 우선순위 큐에 넣어서 나중에 제일 먼저 pop을 해서 얻는 값이
# 0에 가장 가까운 합을 가지는 원소 2개를 얻을 수 있도록 하였다.
# 추가로 원소 하나의 값의 범위가 -10^9 이상 10^9 이하인데,
# 평소 최댓값으로 자주 설정했던 1e9 보다 원소의 합이 큰 경우가 있어서
# heap에 아예 값이 안들어가는 경우가 있었기에 math 라이브러리의 inf를 사용하여 해결하였다.
import sys
import heapq
import math


N = int(input())
solution_value = list(map(int, sys.stdin.readline().split()))
solution_value.sort()
result = math.inf
heap = []
for i in range(len(solution_value) - 1):
    start = i + 1
    end = len(solution_value) - 1
    while start <= end:
        mid = (start + end) // 2
        sum_result = solution_value[i] + solution_value[mid]
        # print(sum_result, solution_value[mid], solution_value[i])
        result = min(result, abs(sum_result))
        if result == abs(sum_result):
            heapq.heappush(heap, (abs(sum_result), i, mid))
            # print(heap)
        if sum_result < 0:
            start = mid + 1
        else:
            end = mid - 1
min_result = heapq.heappop(heap)
print(solution_value[min_result[1]], solution_value[min_result[2]])
