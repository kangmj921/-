# 배열을 M개 이하의 구간으로 나눠서 구간 점수의 최댓값을 최소로 한다.
# 배열의 길이는 최대 5,000이고 나눌 M의 크기도 마찬가지.
# 이분 탐색을 어떻게 활용할지 고민이 많이 된다.
# 전체 조건 중에 최솟값은, 배열이 최대 1개의 원소로 쪼개진 것에서
# 점수를 구하는 것. = 0
# 최댓값은, 배열이 쪼개지지 않고 1개의 구간에서 점수를 구하는 것.
# 점수를 이분탐색하면서, 해당 점수가 최댓값이 될 수 있도록 배열을
# divide했을 떄, divide된 집합의 수가 M개 이하일 경우엔, 점수의
# 구간을 감소시키고, M개 보다 크면 점수의 구간을 증가시켜 찾는다.
# 배열의 크기가 최대 5000으로 크기 않아서 divide_list함수가 시간제한에
# 걸리지 않을 수 있었던 것 같다. 만약 이 함수도 시간제한을 신경써야한다면
# 쪼개진 배열의 최댓값, 최솟값을 기억해놓을 수 있도록 해야될 것이다.
# 이렇게 될경우 최악 시간복잡도는 O(log2(10,000)*5,000)
import sys


def divide_list(target):
    result = []
    for i in num_list:
        if len(result) == 0:
            result.append([i])
            max_in_list = i
            min_in_list = i
        else:
            if max(max_in_list, i) - min(min_in_list, i) <= target:
                result[-1].append(i)
                max_in_list = max(max_in_list, i)
                min_in_list = min(min_in_list, i)
            else:
                result.append([i])
                max_in_list = i
                min_in_list = i
    return len(result)


N, M = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(num_list) - min(num_list)
while start <= end:
    mid = (start + end) // 2
    if divide_list(mid) > M: start = mid + 1
    else: end = mid - 1
print(start)
