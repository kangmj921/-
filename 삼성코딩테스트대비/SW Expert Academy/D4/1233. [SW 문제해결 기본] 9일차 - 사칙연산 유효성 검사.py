# 연산이 불가능한 경우는 data가 사칙연산인 노드가 자식 노드가 2개가 아닐때
# data가 숫자인 노드가 자식 노드를 가질때 두 가지 경우이다.
# 입력을 받을때 바로 확인 가능.
for TC in range(10):
    N = int(input())
    answer = 1
    input_data = []
    for _ in range(N):
        input_data.append(input().split())
    # print(input_data)
    for i in range(len(input_data)):
        if input_data[i][1] in '*+-/':
            if len(input_data[i]) != 4:
                answer = 0
                break
        else:
            if len(input_data[i]) != 2:
                answer = 0
                break
    print("#{} {}".format(TC + 1, answer))
