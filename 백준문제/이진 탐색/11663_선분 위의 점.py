import sys


def binary_search(array, start, end, target):
    print("target : {}".format(target))
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid, True
    return mid, False


N, M = map(int, input().split())
point_list = list(map(int, sys.stdin.readline().split()))
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    a1, a2 = binary_search(point_list, 0, len(point_list) - 1, y)
    b1, b2 = binary_search(point_list, 0, len(point_list) - 1, x)
    print(a1, a2, b1, b2)
    result = a1 - b1
    if a2 and b2:
        result += 1
    if not a2 and not b2:
        result -= 1
    if y > point_list[-1]:
        result += 1
    print(result)
