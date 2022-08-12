# 양수인 두 수를 묶을 때 그 합이 최대가 되려면, 오름차순으로 정렬해놓고 2개의 큰 수끼리 곱을 해야함
# 묶을 때, 큰 수 두 개가 같은 경우, 1을 제외한 나머지는 다 묶었을 때 더 큼.
# 반례로 두 수를 묶을 때, 1이 있으면, 안 묶고 내버려둬서 더하는게 더 큼.


# 음수인 경우, 제일 작은 수 2개를 무조건 묶어야 곱을 했을 때 양수가 됨.
# 만약 2개를 묶지 못하는 상황(1개가 양수)이 되었을땐, 그냥 더하는게 나음
#
from collections import deque
n_list = []
for _ in range(int(input())):
    # 입력 값은 최대 50개
    n_list.append(int(input()))
n_list.sort()
answer = 0
n_list = deque(n_list)
while n_list and n_list[-1] > 0:
    temp1 = n_list.pop()
    if n_list:
        temp2 = n_list.pop()
    else:
        answer += temp1
        break
    if temp1 > 0 and temp2 > 0:
        if temp1 == 1 or temp2 == 1:
            answer += (temp1 + temp2)
        else:
            answer += temp1 * temp2
    else:
        if temp1 <= 0:
            n_list.append(temp1)
        elif temp2 <= 0:
            answer += temp1
        n_list.append(temp2)
        break
while n_list and n_list[0] <= 0:
    temp1 = n_list.popleft()
    if n_list:
        temp2 = n_list.popleft()
    else:
        answer += temp1
        break
    if temp1 <= 0 and temp2 <= 0:
        answer += temp1 * temp2
print(answer)
