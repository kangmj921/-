# 보석을 최대 가치로 훔치려면, 최대한 가치가 높은 것을 훔쳐야한다.
# 최대 가치를 가지는 보석을 선택했을때, 해당 보석의 무게와 가장 근접하면서 큰 제한 무게를 가진
# 가방을 선택해야 최대한 많은 보석을 넣을 수 있다.
# 이 가장 근접하면서 큰 제한 무게를 가진 가방을 찾는 것이 주된 문제이다.
# 가방이 최대 300,000개 이고 보석도 300,000이므로 N * N으로 찾는 것은 시간 제한에 걸림.
# 따라서 N * logN으로 접근을 해야하는데, logN이 되기 위해선
# 우선순위 큐, heapq, BS 등을 활용해야함.
# 그런데 이들을 어떻게 활용해야 될지 고민...

# 가장 근접하면서 큰 제한 무게를 가진 가방을 찾아야하는것이니까
# 최소 힙을 구성하는데, 구성 기준이 무게 보다 큰 제한 무게를 가진 가방임.
# 따라서 무게 제한이 작은 가방은 필요없음.
# 탐색 과정에서 무게 제한이 작은 가방을 어떻게 제외할 수 있을까?
# 그럼 무게 제한이 적은 가방 먼저 채워 넣으면 되긴하는데, 가치가 높은 걸 우선으로 채워야함
# 따라서 보석 리스트에서 현재 가방의 무게 보다 무게가 같거나 작은 보석들을 모두 뽑아
# 최소 힙에 가치의 음수를 넣음. 이렇게 되면 나중에 힙에서 1번 뽑으면 가치가 가장 높은 걸
# 뽑을 수 있음.
# heapq 와 Priorityqueue 모두 logn이지만
# 이렇게 하니까 통과는 하는데, pypy3에서만 됨. python3에서 통과하기 위해서는 최적화가 더 필요함.

# 남은 보석이 없으면 반복을 종료하는 백트래킹을 해줬더니 통과함....
import heapq
import sys


N, K = map(int, input().split())
jewel_list, bag_list = [], []
answer = 0
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewel_list.append([M, V])
jewel_list.sort(reverse=True, key=lambda x: x[0])
for _ in range(K):
    bag_list.append(int(sys.stdin.readline()))
bag_list.sort()
que = []
for i in range(K):
    # python3 에서는 통과 안됨.
    while jewel_list and jewel_list[-1][0] <= bag_list[i]:
        temp = jewel_list.pop()
        heapq.heappush(que, -temp[1])
    if len(que):
        answer += heapq.heappop(que) * -1
    # 추가하니까 됨
    elif not jewel_list:
        break
print(answer)
