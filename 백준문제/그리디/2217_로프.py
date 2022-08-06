# k개의 로프를 이어서 사용할때 버티는 중량은 w/k 이다.
# 최대 중량은 가장 작은 중량을 들 수 있는 로프가 들 수 있는 무게 W, 고른 로프가 K개일 때
# W * K이다.
# 최대의 중량을 얻기 위해선, 가장 작은 중량을 버티는 로프를 하나 고르고
# 그 로프 1개로 버티는 중량 보다 그 다음으로 큰 중량을 버티는 루프가 버티는 중량 * (1 + 1)가 더 크거나 같다면
# 그 다음 큰 중량을 버티는 루프를 선택하고... 아닐 경우 루프 추가를 중단한다.
# 이 과정을 루프 추가를 중단할 때 까지 했을때 구한 중량이 최대 중량이다.

# 반례 하나 때문에 고생을 했다. 하나의 큰 중량을 버티는 로프와, 여러 매우 작은 로프가 모여서 버티는 중량 중
# 후자가 더 클 경우를 내가 생각한 방식으로는 구할 수 없다.
# 왜냐하면 매 1개의 루프를 추가할 때마다 더 작은 로프들은 버려질 것이다.
# 따라서 선택 되지 않은 루프를 저장하는 리스트를 하나 더 따로 만들어서
# 작은 애들이 모여서 현재 최대 중량 보다 클 경우를 추가해주었다.

import sys
from collections import deque


N = int(input())
rope_list = []
selected = []
deselected = []
for _ in range(N):
    rope_list.append(int(sys.stdin.readline()))
rope_list.sort(reverse=True)
rope_list = deque(rope_list)
answer, k = 0, 0
while rope_list:
    temp = rope_list.popleft()
    if answer <= temp * (len(selected) + 1):
        selected.append(temp)
        answer = selected[-1] * (len(selected))
    else:
        deselected.append(temp)
        if answer <= deselected[-1] * (len(deselected) + len(selected)):
            answer = deselected[-1] * (len(deselected) + len(selected))
print(answer)
