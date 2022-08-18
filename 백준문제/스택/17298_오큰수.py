# 맨 마지막 수는 오큰수가 -1로 정해져 있으므로 맨 마지막 수부터 오큰수를 채운다.
# 리스트를 거꾸로 순회하면서, 큐에 마지막으로 넣은 수가 곧 바로 오른쪽의 수이다.
# 큐의 맨 앞의 수는 오른쪽의 수인데, 이 수가 현재 i번째 수보다 클 때 까지 큐에서 뺀다.
# 이 때 큐가 비게 되면, i 번째 수가 가장 크다는 소리이다. 따라서 -1을 결과에 추가한다.
# 그 밖의 경우, 큐의 맨 앞의 수를 결과에 추가한다.
# 그리고 반복의 마지막에 i 번째 수를 큐에 넣는다.
from collections import deque


N = int(input())
N_list = list(map(int, input().split()))
queue = deque()
result_list = deque()
for i in range(N - 1, -1, -1):
    while queue and queue[0] <= N_list[i]:
        queue.popleft()
    if not queue:
        result_list.appendleft(-1)
    else:
        result_list.appendleft(queue[0])
    queue.appendleft(N_list[i])
print(*result_list)
