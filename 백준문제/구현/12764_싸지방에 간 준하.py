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
# 다른 탐색 방법을 사용해야될 것 같다.

import heapq
import sys


N = int(input())
priority_que = []
computer_list = [0] * N
count = [0] * N
answer = 0
stack = []
for _ in range(N):
    P, Q = map(int, sys.stdin.readline().split())
    heapq.heappush(priority_que, [P, Q])
while priority_que:
    temp = heapq.heappop(priority_que)
    check = False
    for i in range(len(computer_list)):
        if computer_list[i] <= temp[0]:
            if not computer_list[i]:
                answer += 1
            computer_list[i] = temp[1]
            count[i] += 1
            break
print(answer)
for i in count:
    if i:
        print(i, end=" ")
