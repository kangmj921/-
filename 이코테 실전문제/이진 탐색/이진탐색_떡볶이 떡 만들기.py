# 이진탐색을 어떻게 활용하느냐가 중요한 문제였다. 찾아야하는 값 M의 범위가 1 <= M <= 2,000,000,000으로
# M을 찾기 위한, 즉 잘라야할 떡의 높이를 이진탐색을 활용해서 풀어야했다.
# 문제를 풀면서 걱정했던 부분은, 한 번 탐색을 해서 높이를 구한 후 잘린 떡의 총 길이를 N이 최대 1,000,000인
# 리스트의 원소를 순차 탐색하며 구하는 부분에서 시간 초과가 나지 않을까 했으나, 이진 탐색으로 M의 값을 탐색하는 횟수가
# 그만큼 줄어 시간 제한에 걸리지 않는 것 같다.
def binary_search(array, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                total += (i - mid)
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


N, M = map(int, input().split())
# rice_cake_height = list(map(int, sys.stdin.readline().split()))
rice_cake_height = [i for i in range(1000000)]
print(binary_search(rice_cake_height, 0, max(rice_cake_height)))
