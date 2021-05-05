# 앞서 푼 문제와 비슷하게 구현해서 풀 수 있었다.
def binary_search(array, start, end):
    global result
    if start > end:
        return result
    else:
        mid = (start + end) // 2
        if array[mid] == mid:
            result = mid
            return result
        binary_search(array, start, mid - 1)
        binary_search(array, mid + 1, end)
        return result


N = int(input())
result = -1
num_list = list(map(int, input().split()))
print(binary_search(num_list, 0, N-1))
