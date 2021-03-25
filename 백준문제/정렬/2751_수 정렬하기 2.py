import sys


def merge(left, right):
    sorted_list = []
    l_index = 0
    r_index = 0
    while len(left) > l_index and len(right) > r_index:
        if left[l_index] <= right[r_index]:
            sorted_list.append(left[l_index])
            l_index += 1
        else:
            sorted_list.append(right[r_index])
            r_index += 1
    sorted_list += right[r_index:]
    sorted_list += left[l_index:]
    return sorted_list


def divide(L):
    if len(L) <= 1: return L
    middle = len(L) // 2
    left_list = L[:middle]
    right_list = L[middle:]
    divide(left_list)
    divide(right_list)
    sorted_list = merge(left_list, right_list)
    for i in range(len(sorted_list)):
        L[i] = sorted_list[i]
    return L


N = int(input())
num_list = list()
for i in range(N):
    num_list.append(int(sys.stdin.readline()))
a = divide(num_list)
for i in a:
    print(i)
