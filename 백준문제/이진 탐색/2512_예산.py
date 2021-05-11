# 배정될 수 있는 예산의 값을 이분 탐색으로 탐색하면서
# 모든 배정된 예산의 값이 총 예산보다 작다면, 탐색 구간을 뒤로
# 아니면 앞으로 해서 배정될 값의 최댓 값을 찾는다.
import sys

N = int(input())
budget_list = list(map(int, sys.stdin.readline().split()))
total_budget = int(input())
start, end = 1, 100000
if sum(budget_list) <= total_budget:
    print(max(budget_list))
    exit()
else:
    while start <= end:
        mid = (start + end) // 2
        result = sum([i if i < mid else mid for i in budget_list])
        if total_budget - result < 0:
            end = mid - 1
        else:
            start = mid + 1
    print(end)
