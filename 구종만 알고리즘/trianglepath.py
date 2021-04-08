import sys


def find_max_(tri_list, n, st):
    if n == 0:
        st[0].append(tri_list[n][0])
        find_max_(tri_list, n + 1, st)
    else:
        if n < len(tri_list):
            ret = 0
            for i in range(n + 1):
                if tri_list[n-1][i] > 0:
                    ret = max(ret, st[n-1][i] + tri_list[n][i])
                if i >= 1 and tri_list[n-1][i - 1] > 0:
                    ret = max(ret, st[n-1][i - 1] + tri_list[n][i])
                st[n].append(ret)
                ret = 0
            find_max_(tri_list, n + 1, st)
        else:
            return


if __name__ == '__main__':
    for C in range(int(sys.stdin.readline())):
        triangle_list = list()
        N = int(sys.stdin.readline())
        for k in range(N):
            triangle_list.append(list(map(int, sys.stdin.readline().split())))
            triangle_list[k].extend(0 for i in range(1, N-k))
        stack = [list() for t in range(N)]
        find_max_(triangle_list, 0, stack)
        print(max(stack[N-1]))