import sys


def solution(c_list):
    min_list = []
    for j in range(len(c_list)):
        a = min(c_list[j])
        if len(min_list) == 0:
            min_list.append(a)
        else:
            if a > min_list[-1]:
                min_list.append(a)
    return min_list[-1]


N, M = map(int, sys.stdin.readline().split())
card_list = []
for i in range(N):
    card_list.append(list(map(int, sys.stdin.readline().split())))
print(solution(card_list))