from collections import deque


def select_num_by_comb(n):
    result = [4, 7]
    for i in range(n):
        pass
    return result


K = int(input())
number_list = select_num_by_comb(11)
number_list.sort()
print(number_list[K - 1])
