import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        n *= factorial(n-1)
    return n


N, K = map(int, sys.stdin.readline().split())
print(int(factorial(N)/(factorial(K)*factorial(N-K))))
