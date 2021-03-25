import sys


def solution(L):
    for i in range(len(L)//2):
        if L[i] != L[len(num_list)-1-i]:
            return 'no'
    return 'yes'


N = int(input())
while N != 0:
    num_list = list(str(N))
    print(solution(num_list))
    N = int(input())
