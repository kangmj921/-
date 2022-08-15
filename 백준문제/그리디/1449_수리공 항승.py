# 구멍의 제일 먼 부분부터 시작해서 각 구간을 확인하며 테이프의 길이를 넘어서 막을 수 있는 경우
# 구간의 시작을 그곳으로 바꾸고 필요한 테이프 수를 하나 더 추가한다.
# 즉, 각 구멍의 구간합이 주어진 테이프의 길이를 넘어가는 경우를 센다.
N, L = map(int, input().split())
answer = 1
N_list = sorted(list(map(int, input().split())))
start = N_list[-1]
for i in range(N - 2, -1, -1):
    result = (start - N_list[i])
    if result >= L:
        answer += 1
        start = N_list[i]
print(answer)
