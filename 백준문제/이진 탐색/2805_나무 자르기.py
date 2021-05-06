# 앞서 풀었던 문제와 동일한 방식으로 진행하였으나 시간초과가
# 계속 발생한다. pypy3으로 제출하게 되면 시간제한에 걸리지않는데,
#
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
start, end = 1, max(tree_list)
while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in tree_list:
        if i >= mid:
            result += (i - mid)
    if result < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
