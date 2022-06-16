# 재귀를 사용하는 과정에서, 한 번 돌린 톱니에 대해 그 옆의 톱니를 참조하는 과정에서
# 이미 1번 참조한 톱니는 참조를 하지 않도록 했어야했는데, 그걸 생각하지 못해서
# 간단한 문제임에도 오랜 시간이 걸리게 되었다.
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)


def rotate_decide(g_n, d, start):  # 기어를 회전시킬때, 양 옆 기어들도 회전하는지 보려면, 리스트의
    # 2, 6 원소를 확인한다. 확인해서 재귀로 해당 기어들도 회전시키는 명령을 내린다.
    polar_2, polar_6 = gear_list[g_n][2], gear_list[g_n][6]
    if d == 1:
        temp = gear_list[g_n].pop()
        gear_list[g_n].appendleft(temp)
    else:
        temp = gear_list[g_n].popleft()
        gear_list[g_n].append(temp)
    if g_n == 1:
        if polar_2 != gear_list[g_n + 1][6] and g_n + 1 != start:
            rotate_decide(g_n + 1, -1 * d, g_n)
    elif g_n == 4:
        if polar_6 != gear_list[g_n - 1][2] and g_n - 1 != start:
            rotate_decide(g_n - 1, -1 * d, g_n)
    else:
        if polar_2 != gear_list[g_n + 1][6] and g_n + 1 != start:
            rotate_decide(g_n + 1, -1 * d, g_n)
        if polar_6 != gear_list[g_n - 1][2] and g_n - 1 != start:
            rotate_decide(g_n - 1, -1 * d, g_n)


gear_list = [[]]
answer = 0
for _ in range(4):
    gear_list.append(deque(map(int, input().rstrip())))
K = int(input())
rotate_list = [list(map(int, input().split())) for _ in range(K)]
visit = [0] * 4
for gear_num, d in rotate_list:
    rotate_decide(gear_num, d, gear_num)
for i in range(1, 5):
    if gear_list[i][0]:
        answer += 2 ** (i - 1)
print(answer)
