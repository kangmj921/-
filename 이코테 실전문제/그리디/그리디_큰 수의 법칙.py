import sys

# 오직 단순히 그리디 알고리즘만 생각한 경우 제일 큰 수를 K번 더하고 그 다음 큰 수를 1번 더하는 것을 반복
# 이 경우로 문제를 풀 경우, 입력 값 M이 엄청 커지게 되면, 시간 초과 판정을 받을 수 있다.
# 시간 초과 판정을 해결하기 위해선, 순열이 반복되는 횟수를 파악해야한다.
# def solution(n_list, m, k):
#     n_list.sort()
#     index = len(n_list) - 1
#     i = 0
#     result = 0
#     while True:
#         if i == m:
#             return result
#         else:
#             if index != len(n_list) - 1:
#                 result += (n_list[index])
#                 i += 1
#                 index += 1
#             else:
#                 result += (n_list[index] * k)
#                 i += k
#                 index -= 1


def solution(n_list, m, k):
    n_list.sort()
    first = n_list[-1]
    second = n_list[len(n_list)-2]
    result = first * k + second
    recur = (m // (k + 1))
    result += first * (m % (k + 1))
    result *= recur
    return result


N, M, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
print(solution(num_list, M, K))
