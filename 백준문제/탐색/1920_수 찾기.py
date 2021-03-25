import sys


def solution(L, x):
    upper = len(L) - 1
    lower = 0
    while lower <= upper:
        target = (upper + lower) // 2
        if L[target] > x:
            upper = target - 1
        elif L[target] < x:
            lower = target + 1
        else:
            return 1
    return 0


N = int(input())
num_list = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())
check_list = list(map(int, sys.stdin.readline().split()))
for i in check_list:
    print(solution(num_list, i))
