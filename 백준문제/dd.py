from collections import deque
d_index = [-1, 1]


def BFS(array, target_index):
    queue = deque()
    queue.append(target_index)
    visited = [0] * len(array)
    while queue:
        present_index = queue.popleft()
        for i in range(2):
            next_index = present_index + d_index[i]
            if 0 <= next_index < len(array):
                if array[next_index] > array[target_index]:
                    return next_index
                elif visited[next_index] == 0:
                    visited[next_index] = 1
                    queue.append(next_index)
    return -1


def solution(array):
    answer = []
    a = -1
    print(len(array))
    for i in range(len(array)):
        if a != array[i]:
            result = BFS(array, i)
        if result == -1:
            a = array[i]
        answer.append(result)
    return answer


print(len(solution([i for i in range(100000)])))
