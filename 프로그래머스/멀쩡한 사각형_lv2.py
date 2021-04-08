import math


def solution(w, h):
    answer = w * h
    return answer - (w + h - math.gcd(w, h))


T = int(input())
for i in range(T):
    w, h = map(int, input().split())
    print(solution(w, h))
