# 평범한 완전탐색문제, 재귀를 이용하여 풀 수 있었다.
import sys


def search(idx, n):
    if n == 6:
        print(*stack)
        return
    for i in range(idx, len(S)):
        if not visited[i]:
            visited[i] = 1
            stack.append(S[i])
            search(i + 1, n + 1)
            stack.pop()
            visited[i] = 0


while True:
    input_s = sys.stdin.readline().split()
    K = int(input_s[0])
    if not K:
        exit()
    S = list(map(int, input_s[1:]))
    stack = []
    visited = [0] * len(S)
    search(0, 0)
    print()