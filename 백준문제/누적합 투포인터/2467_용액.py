from queue import PriorityQueue


N = int(input())
liquid_list = list(map(int, input().split()))
start, end = 0, N - 1
que = PriorityQueue()
while start < end:
    result = liquid_list[start] + liquid_list[end]
    que.put((abs(result), [liquid_list[start], liquid_list[end]]))
    if result < 0:
        start += 1
    else:
        end -= 1
print(*que.get()[1])
