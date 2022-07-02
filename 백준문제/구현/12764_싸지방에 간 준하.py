# 우선순위 큐를 이용하는 건 맞는데 구현이 잘 정리가 안된다.
# 일단 입력 받은대로 우선순위 큐를 구성하게 되면, 시작시간을 기준으로
# 제일 빠른 시작시간이 앞에 위치하게 된다.
# 우선순위 큐에서 위에서 부터 하나씩 빼면서, computer_list에 넣어주는데
# computer_list에 들어가있는 종료시간들이 현재 우선순위 큐에서 뺀 시작시간 보다 클 때 까지
# index를 구하면. 그게 곧 컴퓨터 자리가 비는 제일 빠른 index 번호이다.
# 만약 index에 해당하는 computer_list의 값이 0이라면 컴퓨터를 하나 추가해야하는 상황이다.
# 그러므로 해당 index에 종료시간을 초기화하고 컴퓨터의 수를 저장한 변수 + 1
# 아니라면, 해당 index에 해당하는 컴퓨터를 쓸 수 있으므로, 해당 index에 해당하는 count의 원소 + 1

# python3에서는 계속 시간초과가 나지만, pypy3에선 안난다.
# 비는 컴퓨터 자리를 찾는 탐색 방법을 미리 자리를 저장해 놓는 방식으로 바꿔야 할 것 같다.
# 먼저 시작 시간에 따라 사람의 컴퓨터 이용 시간을 정렬한 뒤, 먼저 온 사람대로 젤 왼쪽의 컴퓨터를
# 배정하는데, 우선순위 큐에 배정된 사람의 종료시간과 배정받은 컴퓨터 번호를 저장하는 리스트를 넣는다.
# 이러면, 우선순위 큐에는 젤 먼저 종료하는 사람의 종료 시간과 컴퓨터 번호가 젤 위에 오게 될 것이다.
# 
#
import heapq
import sys


N = int(input())
priority_que = []
computer_list = [i for i in range(1, N + 1)]
time_list = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_list.sort(key=lambda x: x[0])
count = [0] * (N + 1)
answer = 0
for P, Q in time_list:
    while priority_que and priority_que[0][0] < P:
        temp = heapq.heappop(priority_que)
        heapq.heappush(computer_list, temp[1])
    nxt = heapq.heappop(computer_list)
    heapq.heappush(priority_que, (Q, nxt))
    count[nxt] += 1
    if len(priority_que) > answer:
        answer = len(priority_que)
print(answer)
for i in count:
    if i:
        print(i, end=" ")

# 기존에 시간초과 되었던 풀이
# for _ in range(N):
#     P, Q = map(int, sys.stdin.readline().split())
#     heapq.heappush(priority_que, [P, Q])
# while priority_que:
#     temp = heapq.heappop(priority_que)
#     for i in range(len(computer_list)):
#         if computer_list[i] <= temp[0]:
#             if not computer_list[i]:
#                 answer += 1
#             computer_list[i] = temp[1]
#             count[i] += 1
#             break