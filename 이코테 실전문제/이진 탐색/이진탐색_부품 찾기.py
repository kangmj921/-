import sys


def bin_search(start, target, end, array):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
    return False


N = int(input())
store_part_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
request_part_list = list(map(int, sys.stdin.readline().split()))
store_part_list.sort()
for i in request_part_list:
    if bin_search(0, i, len(store_part_list) - 1, store_part_list):
        print("yes", end=" ")
    else:
        print("no", end=" ")
