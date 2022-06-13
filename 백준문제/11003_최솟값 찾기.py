# L과 N의 최대 범위는 5,000,000, N개의 수는 각자의 크기의 범위가 2 * 10 ^ 9임.
# Di는 n_list 에 저장된 값 중 i - L + 1번째부터 연속된 L개의 값 가장 최소의 값이다.
# Di를 구하려면, N개의 원소 모두 조회해야하므로 무조건 O(N)
# 각 O(N)에 대해서 연속된 L개의 값 중 최소를 찾는 과정이 적어도 O(N) 보다는 적어야함.
#
# i번째 원소를 조회하면서 우선순위 큐에 값과 인덱스값 한 쌍을 넣는다. i - L + 1 <= 0이면
# 최솟값은 무조건 우선순위 큐의 맨 앞 원소이다. 각 원소를 추가하거나 삭제하는데 heap은 O(logn)이므로
# 최대 시간 복잡도는 O(NlogN)이다.
# 범위의 시작을 항상 구해놓고, 큐의 맨 앞 원소에 저장된 범위가 범위의 시작보다 작을 경우
# 큐에서 계속 빼준다.

# 제출해보니 파이썬3으로는 시간초과가 걸리고, pypy3은 시간초과에 걸리지 않았다.
# 파이썬3으로 제출할때는 더 빠른 O(1)으로 해야될 것 같다.
# O(1)으로 하기 위해선, 삽입과 삭제가 왼쪽 오른쪽 자유로운 deque 를 쓰면 될 것이다.
import sys
import heapq
from collections import deque


N, L = map(int, input().split())
n_list = list(map(int, sys.stdin.readline().split()))
# que = []
# for i in range(N):
#     left = i - L + 1
#     while que and que[0][1] < left:
#         heapq.heappop(que)
#     heapq.heappush(que, (n_list[i], i))
#     sys.stdout.write(str(que[0][0]) + ' ')
queue = deque()
for i in range(N):
    left = i - L + 1
    while queue and queue[0][1] < left:
        queue.popleft()
    while queue and queue[-1][0] > n_list[i]:
        queue.pop()
    queue.append((n_list[i], i))
    sys.stdout.write(str(queue[0][0]) + ' ')
