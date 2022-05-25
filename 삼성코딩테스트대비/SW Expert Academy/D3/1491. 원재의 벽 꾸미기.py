import math


def solution(r, c):
    global answer
    for i in range(r, N + 1):
        for j in range(c, N + 1):
            if i * j <= N:
                answer = min(answer, A * abs(i - j) + B * (N - i * j))
            else:
                break


for T in range(int(input())):
    N, A, B = map(int, input().split())
    answer = math.inf
    solution(1, 1)
    print("#{} {}".format(T + 1, answer))
