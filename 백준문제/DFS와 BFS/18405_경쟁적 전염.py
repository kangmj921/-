# 처음 바이러스의 종류가 낮은 것 부터 빠져나오도록 하는 우선순위 큐에 바이러스의
# 위치를 넣은 후, BFS를 돌릴것이다. BFS를 돌리는 과정에서 토마토 문제와 같이
# 1초 마다 생기는 마지막 바이러스의 위치가 pop되면 1초가 지난 것으로 구현할 예정이다.
# heapq를 사용하는 과정에서 문제가 있었다. 힙은 부모가 두 자식들 보다 크지 않음을
# 보장하는 것이지 자식들간의 대소는 보장하지 않았다. 큐내의 가장 작은 원소를 빠르게 찾는 것이
# 목적인 것이지 전체가 우선순위 대로 정렬되는 것과는 무관한 자료구조였던 것이다!!
from collections import deque

N, K = map(int, input().split())
experience_map = []
for i in range(N):
    experience_map.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())
time_pass = 0
virus_list = []
for i in range(N):
    for j in range(N):
        if experience_map[i][j] != 0:
            virus_list.append([experience_map[i][j], i, j])
virus_list.sort(key=lambda x:x[0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
heap = deque(virus_list)
if len(heap) != 0:
    time_pass_std = heap[-1]
else:
    print(0)
    exit()
while time_pass < S:
    if len(heap) != 0:
        k, y, x = heap.popleft()
    else:
        print(experience_map[X-1][Y-1])
        exit()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        if experience_map[ny][nx] != 0:
            continue
        if experience_map[ny][nx] == 0:
            experience_map[ny][nx] = k
            heap.append([k, ny, nx])
    if [k, y, x] == time_pass_std:
        time_pass += 1
        if len(heap) != 0:
            time_pass_std = heap[-1]
print(experience_map[X - 1][Y - 1])
