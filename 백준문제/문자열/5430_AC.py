# 33퍼센트에서 계속 틀리길래, 모든 경우에 대해 반레를 찾아봐서 확인했지만 계쏙 틀렸다.
# 아무래도 출력 결과에 대한 문제인거 같아서 찾아보았지만 아니었고, 마지막에 결과를 출력할때,
# reverse 하지 않아서 그런거였다...
from collections import deque


for T in range(int(input())):
    # T는 최대 100번
    p = input().rstrip()
    # P의 길이는 최대 10 ^ 5
    n = int(input())
    input_str = input().rstrip()
    if p.count('D') > n:
        print('error')
        continue
    n_list = deque(input_str[1:-1].split(','))
    pop_index = -1
    for command in p:  # 명령어가 R 일때, n_list 를 뒤집는 과정을
        # 최대 O(1) 정도로 해줘야 R만 10^5개가 나올 때, 시간제한 통과
        # R이 한번 나올때 D에서 참조하는 index 를 len(n_list) -1 -1 -1로 찾을 수 있게 하고
        # 다시 R이 한번 나오면 index 를 0 len(n_list)로 하면??
        # n_list 의 자료구조가 deque 인 경우 왼쪽, 오른쪽에서 pop 이 자유롭다.
        # print(n_list, command)
        if command == 'R':
            pop_index *= -1
        else:
            if pop_index == -1:
                n_list.popleft()
            else:
                n_list.pop()
    if pop_index == 1:
        n_list.reverse()
    print('[' + ','.join(n_list) + ']')
