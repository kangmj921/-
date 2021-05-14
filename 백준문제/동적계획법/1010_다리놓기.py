import time


def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def solution(x, y):
    return factorial(y) // (factorial(x) * factorial(y - x))


start = time.time()
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(solution(N, M))
