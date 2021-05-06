def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
M = int(input())
check_list = list(map(int, input().split()))
for i in check_list:
    print(binary_search(num_list, 0, N - 1, i))
