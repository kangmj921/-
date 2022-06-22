# 중요도가 높은 문서가 하나라도 있다면, 문서를 queue의 가장 뒤에 재배치해야하고, 그렇지 않다면
# queue의 가장 앞의 문서를 인쇄(pop)해야 하므로, 리스트의 맨 앞의 원소를 삭제하는데 O(N)의 시간이 걸린다.
#
#
import heapq
from collections import deque


for _ in range(int(input())):
    num_of_documents, target_document = map(int, input().split())
    input_list = deque(map(int, input().split()))
    document_list = deque()
    que = []
    i = 0
    for d in input_list:
        heapq.heappush(que, (-1 * d))
        document_list.append([d, i])
        i += 1
    answer = 0
    i = 0
    while document_list:
        if -1 * que[0] > document_list[i][0]:
            document_list.append(document_list.popleft())
        else:
            heapq.heappop(que)
            c = document_list.popleft()
            answer += 1
            if c[1] == target_document:
                print(answer)
