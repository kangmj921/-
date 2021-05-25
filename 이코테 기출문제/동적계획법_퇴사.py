# 맨 뒤에서 부터 다이나믹 프로그래밍을 진행한다.
# 뒤쪽 날짜부터의 상담에 대해여 현재 상담일자의 이윤(present_pay) +
# 현재 상담을 마친 일자부터의 최대이윤(dp_list[i + present_day])을 계산하고
# 이후에 계산된 각각의 값 중 최댓값을 저장하면 된다.
# dp_list[i] = i 번째 날 부터 마지막 날까지 낼 수 있는 최대 이익이라고 하면,
# 점화식은 dp_list[i] = max(present_pay + dp_list[i + present_day], max_value)이다.
# 이 때, max_value는 현재까지의 최대 상담 금액에 해당하는 것이므로, dp_list[i + 1]과 같다.
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
