# 앞서 풀었던 두 용액 문제에서 한 가지 용액을 더 추가하는 조건이 붙은 문제이다.
# 용액의 수가 최대 5000으로 줄어서, 최악 O(N*N*logN)의 시간이 걸려도
# 25,000,000*logN으로 pypy3으로 제출하였을땐, 아슬아슬하게 통과를 할 수 있었지만, python3로는
# 시간초과가 걸렸다. python3로 통과한 사람들의 코드를 살펴보니, 투 포인터를 활용하였다.
# 선택할 1개의 용액은 리스트의 원소 하나씩 선택하고
# 나머지 2개의 용액은 처음 선택한 1개의 용액 다음 용액과 젤 큰 수의 용액을 선택하고
# 합을 구한 뒤, 합이 0보다 작으면 두 번째 선택한 용액의 오른쪽 용액을 선택하고
# 0보다 크다면 3번쨰 선택한 용액의 왼쪽 용액을 선택하는 방식으로 하였다.
# 이렇게 한다면 최악 시간 복잡도 O(N*N)을 얻을 수 있을 것 같다.
import sys
import math


N = int(input())
solution_value = list(map(int, sys.stdin.readline().split()))
result = math.inf
solution_value.sort()
for i in range(N - 2):
    first = solution_value[i]       # 투 포인터 활용
    second = i + 1
    third = N - 1
    check = False
    while second < third:
        sum_result = first + solution_value[second] + solution_value[third]
        if result >= abs(sum_result):
            result = abs(sum_result)
            re_a, re_b, re_c = i, second, third
        if sum_result > 0:
            third -= 1
        elif sum_result < 0:
            second += 1
        else:
            check = True
            break
    if check:
        break
    # for j in range(i + 1, N - 1):     # 이분 탐색 활용 python3에선 시간초과
    #     start = j + 1
    #     end = N - 1
    #     while start <= end:
    #         mid = (start + end) // 2
    #         sum_result = solution_value[i] + solution_value[j] + solution_value[mid]
    #         if result >= abs(sum_result):
    #             result = abs(sum_result)
    #             re_a, re_b, re_c = i, j, mid
    #         if sum_result > 0:
    #             end = mid - 1
    #         elif sum_result < 0:
    #             start = mid + 1
    #         else:
    #             break
for index in [re_a, re_b, re_c]:
    print(solution_value[index], end=" ")
