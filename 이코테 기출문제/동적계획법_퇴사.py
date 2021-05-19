# 맨 뒤에서 부터 다이나믹 프로그래밍을 진행한다.
# 진행되는 날짜가 선택되려면, 해당 일 수 가 넘어가지않도록 하는 기간을 가진
# 상담 일정 중에 상담 기간이 가장 길거나, 금액이 가장 큰 것을 계속 고르면 된다.
N = int(input())
schedule_list = []
for _ in range(N):
    schedule_list.append(list(map(int, input().split())))
dp_list = [0] * N
for i in range(N - 1, -1, -1):
    present_pay = schedule_list[i][1]
    present_day = schedule_list[i][0]
    if present_day > N - i:
        if i != N - 1:
            dp_list[i] = dp_list[i + 1]
        continue
    if i == N - 1:
        dp_list[i] = present_pay
    elif i + present_day == N:
        dp_list[i] = max(present_pay, dp_list[i + 1])
    else:
        dp_list[i] = max(present_pay + dp_list[i + present_day], dp_list[i + 1])
print(max(dp_list))
