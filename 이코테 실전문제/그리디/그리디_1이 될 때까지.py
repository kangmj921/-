import sys
import math


def solution(n, k):
    result = 0
    while n >= k:
        if n % k != 0:
            result += (n % k)
            n -= (n % k)
        result += 1
        n /= k
    result += (n - 1)
    return result


N, K = map(int, sys.stdin.readline().split())
print(int(solution(N, K)))
