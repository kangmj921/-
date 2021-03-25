import sys


def pre_order(p_t, i_t, i):
    standard = i_t.index(p_t[i])
    left_sub = i_t[:standard]
    right_sub = i_t[standard+1:]
    if left_sub and right_sub:
        print(i_t[standard], end=" ")
    if left_sub:
        pre_order(p_t, left_sub, i + 1)
    if right_sub:
        pre_order(p_t, right_sub, i + 1 + len(left_sub))
    if not left_sub or not right_sub:
        print(i_t[standard], end=" ")
        return


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    in_order_traverse = list(map(int, sys.stdin.readline().split()))
    post_order_traverse = list(map(int, sys.stdin.readline().split()))
    pre_order(in_order_traverse, post_order_traverse, 0)
    print()