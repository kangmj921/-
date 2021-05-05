# 이진 탐색을 재귀 함수를 이용해서 구현하는데, 재귀 함수 안에서 재귀 함수를 2번 호출하는 과정이
# 매끄럽게 구현이 되지 않아 애를 먹었다. 2번 호출하고 나서 끝마친 재귀는 반환을 통해 종료를 시켜줘야
# 하는데 그러지 못해서 무한히 재귀를 돌게 되었다. 다음 부터는 재귀 함수의 종료에 대해 더 신경써서
# 구현을 해야 될 것 같다.
def binary_search(array, start, end):
    global result
    if len(array) == 0:
        return result
    elif len(array) == 1:
        return result
    else:
        mid = (start + end) // 2
        if array[mid] == x:
            result += 1
        left, right = array[start:mid], array[mid:]
        binary_search(left, 0, len(left))
        binary_search(right, 0, len(right))
        return result


result = 0
N, x = map(int, input().split())
num_list = list(map(int, input().split()))
binary_search(num_list, 0, N)
if result == 0:
    print(-1)
else:
    print(result)
