#처음 부모 노드를 기준으로 왼쪽 오른쪽 나눠서
#재귀형식으로 계속 들어가서 왼쪽 자식-> 오른쪽 자식 -> 부모
#순으로 출력하도록 함.
#
#         27
# 9 12 16    36 54 72
#
#         16
#    9 12
#
#          9
#              12
#
#         12
#
#         54
#      36    72
import sys


def post_order(p_t, i_t, i):
    standard = i_t.index(p_t[i])
    left_sub = i_t[:standard]
    right_sub = i_t[standard+1:]
    if left_sub:
        post_order(p_t, left_sub, i + 1)
    if right_sub:
        post_order(p_t, right_sub, i + 1 + len(left_sub))
    if left_sub and right_sub:
        print(i_t[standard], end=" ")
    if not left_sub or not right_sub:
        print(i_t[standard], end=" ")
        return


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        N = int(sys.stdin.readline())
        pre_order_traverse = list(map(int, sys.stdin.readline().split()))
        in_order_traverse = list(map(int, sys.stdin.readline().split()))
        post_order(pre_order_traverse, in_order_traverse, 0)
        print()
