import sys


def solution(b, f):
    visited = []
    for i in b:

        pass


T = int(input())
for i in range(T):
    baechu_position = []
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0 for i in range(M)] for j in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        baechu_position.append([x, y])
        farm[y][x] = 1
    solution(baechu_position, farm)
