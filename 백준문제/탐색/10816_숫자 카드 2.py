import sys


# 이분 탐색으로 nlog(n)까지의 시간복잡도를 기대할 수 있다.
# 완전 탐색으로 한다면 n^2의 시간복잡도를 가진다.
# 이분 탐색 구현하기 익히자!
# 딕셔너리 자료형만으로 더 빨리 구현이 가능하다.

##이분 탐색
# def search_num(c, n):
#     upper = len(c) - 1
#     lower = 0
#     while upper >= lower:
#         target = (upper + lower) // 2
#         if c[target] < n:
#             lower = target + 1
#         elif c[target] > n:
#             upper = target - 1
#         else:
#             return 1
#     return 0

# N = int(input())
# card_list = list(map(int, sys.stdin.readline().split()))
# M = int(input())
# num_list = list(map(int, sys.stdin.readline().split()))
# n_list = sorted(num_list)
# result = dict()
#
# for i in card_list:
#     num = search_num(n_list, i)
#     if num and not i in result:
#         result[i] = num
#     elif num and result[i] != 0:
#         result[i] += num
#
# for j in num_list:
#     try:
#         print(result[j], end=" ")
#     except:
#         print(0, end=" ")


##딕셔너리 이용
N = int(input())
card_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
n_list = sorted(num_list)
result = dict()

