import sys


def rotation(k, m):
    for y, x in k:
        
        pass


def solution(key, lock):
    temp1 = []
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                x, y = i, j
                temp1.append((x, y))
    temp1 = rotation(temp1, len(key))
    print(temp1)
    return None


N, M = map(int, input().split())
key_list, lock_list = [], []
for i in range(N):
    key_list.append(list(map(int, sys.stdin.readline().split())))
for i in range(M):
    lock_list.append(list(map(int, sys.stdin.readline().split())))
print(solution(key_list, lock_list))
