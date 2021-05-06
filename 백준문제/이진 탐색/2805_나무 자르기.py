# 앞서 풀었던 문제와 동일한 방식으로 진행하였으나 시간초과가
# 계속 발생한다. pypy3으로 제출하게 되면 시간제한에 걸리지않는데,
# 파이썬의 경우 찾아본 결과 tree_list의 모든 원소를 돌며 result를
# 구하는 과정 때문에 그렇다고 한다.
# 이 문제를 해결한 사람들의 경우
# result = sum([i-mid if mid < i else 0 for i in tree_list])로
# 해결하였는데, List comprehension을 이용해서 조건에 맞는 원소들만
# 갖는 리스트를 기존(원소 하나씩 참고하는 식)보다 빠르게
# 만들어낼 수 있어서 그렇다고 한다.
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))
start, end = 1, max(tree_list)
while start <= end:
    result = 0
    mid = (start + end) // 2
    # for i in tree_list:
    #     if i >= mid:
    #         result += (i - mid)
    result = sum([i-mid if mid < i else 0 for i in tree_list])
    if result < M:
        end = mid - 1
    else:
        start = mid + 1
print(end)
