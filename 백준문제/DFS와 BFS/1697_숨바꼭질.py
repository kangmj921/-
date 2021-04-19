from collections import deque


# BFS를 이용하여 최단 시간을 구하는 문제로, 한 번 갔던 곳은 다시 갈 필요가 없기에
# 기록해 주는 것이 중요하다. 안 그러면 시간초과남.
N, K = map(int, input().split())
result = 0
queue = deque()
queue.append(N)
time_labs = queue[-1]
visited = [0] * 1000001
visited[N] = 0
while queue:
    present = queue.popleft()
    if present == K:
        print(result)
        exit()
    move_list = [-1, 1, present]
    for i in range(3):
        next = present + move_list[i]
        if next - present > K:
            continue
        if next < 0:
            continue
        if visited[next] == 0:
            visited[next] = 1
            queue.append(next)
    if present == time_labs:
        # print(time_labs, queue)
        time_labs = queue[-1]
        result += 1
print(result)
