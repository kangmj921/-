import sys


def get_LIS(n_list):
    if len(n_list) == 0:
        return 0
    ret = 0
    for i in range(len(n_list)):
        stack = list()
        for j in range(i+1, len(n_list)):
            if n_list[i] < n_list[j]:
                stack.append(n_list[j])
        #print(n_list, ret, stack)
        ret = max(ret, 1 + get_LIS(stack))
    return ret


for C in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    print(get_LIS(num_list))
