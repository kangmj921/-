# 선분 위의 점의 개수를 알아야하기 때문에, 선분에서 가장 왼쪽의 점, 가장 오른쪽의 점의 index를 구해서
# 가장 오른쪽 점의 index에서 가장 왼쪽의 index를 빼면 점의 개수를 구할 수 있다.
# 가장 오른쪽의 점이 선분 위에 있는 경우, 벗어난 경우와 가장 왼쪽의 점이 선분위인 경우, 벗어난 경우를
# 구분하야 구하면 된다.
import sys


def binary_search(array, line_start, line_end):
    start = 0
    end = len(array) - 1
    while start <= end:
        left = (start + end) // 2
        if line_start <= array[left] <= line_end:
            end = left - 1
        else:
            if array[left] < line_start:
                start = left + 1
            elif array[left] > line_end:
                end = left - 1
    start = 0
    end = len(array) - 1
    while start <= end:
        right = (start + end) // 2
        if line_start <= array[right] <= line_end:
            start = right + 1
        else:
            if array[right] < line_start:
                start = right + 1
            elif array[right] > line_end:
                end = right - 1
    if array[left] >= line_start and array[right] <= line_end:
        return right - left + 1
    if array[left] < line_start and array[right] > line_end:
        return right - left - 1
    return right - left


N, M = map(int, input().split())
point_list = list(map(int, sys.stdin.readline().split()))
point_list.sort()
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    print(binary_search(point_list, x, y))
