# 글자의 수가 최대 11개 이므로, 사이에 끼워넣는 연산자의 수는 10개이다.
# 연산자의 종류는 총 4가지 이므로, 최악 시간복잡도가 4 ** 10으로 백만 정도이다.
# 따라서 완전탐색으로 문제를 해결했다.
import sys
import math


def search(a, s, m, d, idx, total):
    global answer1, answer2
    # print(a, s, m, d, total)
    if idx == N:
        answer1 = max(answer1, total)
        answer2 = min(answer2, total)
        return
    if a > 0:
        search(a - 1, s, m, d, idx + 1, total + num_list[idx])
    if s > 0:
        search(a, s - 1, m, d, idx + 1, total - num_list[idx])
    if m > 0:
        search(a, s, m - 1, d, idx + 1, total * num_list[idx])
    if d > 0:
        if total < 0:
            temp = (abs(total) // num_list[idx]) * -1
        else:
            temp = total // num_list[idx]
        search(a, s, m, d - 1, idx + 1, temp)


N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
answer1, answer2 = -1 * math.inf, math.inf
add, sub, mul, div = map(int, input().split())
search(add, sub, mul, div, 1, num_list[0])
print(answer1)
print(answer2)
