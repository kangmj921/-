import sys
import copy


# 3800ms의 실행시간으로 통과를 했다. 제한 시간이 3초라 넉넉한 편이었지만,
# 더 빠른 실행시간을 가진 사람들의 코드를 보니 queue 라이브러리를 이용하였다.
def rotation_45(n_list, direction):
    temp = copy.deepcopy(n_list)
    if direction < 0:
        for i in range(n):
            temp[int(n/2)][i] = n_list[i][i]
            temp[n-1-i][i] = n_list[int(n/2)][i]
            temp[i][int(n/2)] = n_list[i][n-1-i]
            temp[i][i] = n_list[i][int(n/2)]
    else:
        for i in range(n):
            temp[int(n / 2)][i] = n_list[n-1-i][i]
            temp[i][i] = n_list[int(n/2)][i]
            temp[i][int(n/2)] = n_list[i][i]
            temp[i][n-1-i] = n_list[i][int(n/2)]
    n_list = temp
    return n_list


T = int(input())
for i in range(T):
    n, d = map(int, sys.stdin.readline().split())
    num_list = []
    d /= 45
    for i in range(n):
        num_list.append(list(map(int, input().split())))
    for i in range(int(abs(d))):
        num_list = rotation_45(num_list, int(d))
    for i in range(n):
        for j in range(n):
            print(num_list[i][j], end=" ")
        print()
