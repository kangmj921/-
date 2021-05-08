# 이진탐색이나 BFS로 접근이 가능할 것이다. 하지만 BFS의 경우는
# 그래프를 인접 행렬로 구현하게 되면 최악 O(100,000 * 100,000)으로
# 시간 제한을 만족하지 못한다. 따라서 linked list로 구현을 해야
# O(100,000 + 100,000)만 큼이 될 것이다.
# 이진탐색으로 어떻게 구현을 해야 할지 생각해봐야 될 것 같다.
# 우선 C의 값을 기준으로 오름 차순 정렬을 한 뒤,
# 출발점이나 도착점이 a 인 것 중 제일 큰 무게 제한을 가진 다리를 찾고,(최대 O(100,000))
# 그 다리의 도착점이 b면 함수 종료, 아니면 기록해둠.
# 그 다리의 index 기준으로 자르고 자른 배열안에서 출발점이나 도착점이
# 기록해둔 값인 것 중 가장 큰 무게 제한을 가진 다리를 찾고
# 반복...하면 값을 찾을 수 있을까?
#
import sys
from bisect import bisect_right, bisect_left
import heapq


N, M = map(int, input().split())
bridge_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
a, b = map(int, input().split())
bridge_list.sort(key=lambda x: x[2])
index = 0
for i in range(index, M):
    result = 0
    if bridge_list[i][0] == a or bridge_list[i][1] == a:
        result = max(result, bridge_list[i][2])
        if result == bridge_list[i][2]:
            if bridge_list[i][1] == b:
                break
            else:
                a = bridge_list[i][0]
            index = i
print(bridge_list)
