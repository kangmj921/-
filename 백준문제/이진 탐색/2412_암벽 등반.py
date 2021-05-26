# 이분탐색 태그가 붙어 있어, 이분탐색을 어떻게 활용해야 되는지
# 생각해 봐야 할 것 같다. 이동할 수 있는 범위는 x, y 각각
# 2 차이나는 것으로 이동할 수 있음.
# 이분탐색으로 다음 이동할 수 있는 점을 찾아서 계속 이동하다가
# y좌표가 T와 같으면 탐색을 종료해서 최소 이동 횟수를 출력?

import sys


n, T = map(int, input().split())
point_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
point_list.sort()
print(point_list)
start, end = 0, len(point_list) - 1
while start <= end:
    mid = (start + end) // 2
    break
