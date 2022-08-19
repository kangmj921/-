# 골라야 하는 초밥의 수는 k개로 일정하므로 슬라이딩 윈도우를 이용해서 구한다.
# 슬라이딩 윈도우를 통해 구한 초밥 리스트에서 쿠폰으로 무료로 먹을 수 있는 초밥도 추가하고
# 그 결과를 set을 활용해서 초밥 종류의 개수를 구한 뒤 최대 값을 찾는다.
# 이 과정에서 초밥의 결과를 반복마다 저장하고 한꺼번에 set 연산자로 결과를 찾았는데
# 메모리 초과가 나서 최적화를 진행하였다.
# 
from collections import deque
import sys


N, d, k, c = map(int, input().split())
chobab_list = []
for _ in range(N):
    chobab_list.append(int(sys.stdin.readline()))
result_list = chobab_list[:k]
answer = len(set(result_list + [c]))
for i in range(1, N):
    end = (i + k - 1) % N
    result_list = deque(result_list)
    result_list.popleft()
    result_list.append(chobab_list[end])
    temp = list(result_list) + [c]
    answer = max(answer, len(set(temp)))
print(answer)
