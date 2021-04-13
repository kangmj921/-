# 그냥 재귀와 배열의 원소를 하나하나 찾으면서 구현할 경우 시간초과....
# 최악의 경우 O(n!)의 시간복잡도 때문이다.
# 다른 방법을 이용하자.
# 우선순위 큐를 이용하여 구현하기로 했다. 우선순위 큐는
# 데이터의 개수가 N일 때 삽입, 삭제 하는데 NlogN의 시간복잡도를 가져서 N이 매우 큰 경우 유리하다.
# heapq를 이용한 힙 구현을 잘 알아야겠다.
# heapq를 이용하는 중에도 시간초과가 되는 경우가 있었다. 이때, 함수로 호출해서 heapq를 사용하는 부분을
# 함수를 호출하지 않고 사용하는 쪽으로 바꿨는데 시간초과가 걸리지 않았다.
# 입력 개수가 많아 시간 제한이 빡빡한 경우, 입력 속도에 따라 차이가 나는거 같다.
# 코딩 테스트에서는 sys 라이브러리를 사용하지 못한다는데, 이거를 고려해서 시간 제한을 주지 않을까 싶다.
import heapq
import sys


N = int(input())
lecture_list = []
for i in range(N):
    lecture_list.append(list(map(int, sys.stdin.readline().split())))
lecture_list.sort(key=lambda x: x[0])
heap = []
heapq.heapify(heap)
heapq.heappush(heap, lecture_list[0][1])
for i in range(1, N):
    if lecture_list[i][0] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lecture_list[i][1])
# print(heap)
print(len(heap))
