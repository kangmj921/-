import sys


def solution(N, l):
    count = 0
    for i in range(1, N + 1):
        current = i
        while current != 0:
            if l[current] == 0:
                if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                    l[current] += 1
            n = current // 10
            if l[n] != 0:
                l[current] += l[n]
                current = 0
            current = current // 10
    return l


N = int(input())
n_list = [0 for i in range(N+1)]
print(sum(solution(N, n_list)))
