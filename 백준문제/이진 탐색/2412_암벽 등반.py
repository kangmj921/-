import sys


n, T = map(int, input().split())
point_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
present_x, present_y = 0, 0
move_count = 0

