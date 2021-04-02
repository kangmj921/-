import sys


# 3 x 3 행렬을 한 칸씩 이동시키면서 바꿔야할 행렬과 다른 부분이 있으면 전부 뒤집으면서
# 진행시킴.
def solution():
    result = 0
    for i in range(N - 2):
        for j in range(M - 2):
            if not boolean_list[i][j]:
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        boolean_list[k][l] = not boolean_list[k][l]
                result += 1
    for i in range(N):
        for j in range(M):
            if not boolean_list[i][j]:
                return -1
    return result


N, M = map(int, sys.stdin.readline().split())
result = 0
A_list, B_list = list(), list()
boolean_list = [[0] * M for i in range(N)]
for i in range(N):
    A_list.append(list(map(int, sys.stdin.readline().rstrip('\n'))))
for i in range(N):
    B_list.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

for i in range(N):
    for j in range(M):
        boolean_list[i][j] = A_list[i][j] == B_list[i][j]

if N >= 3 and M >= 3:
    print(solution())
else:
    for i in range(N):
        for j in range(M):
            if not boolean_list[i][j]:
                print(-1)
                exit()
    print(0)
