# 맨 뒤에서 부터 다이나믹 프로그래밍을 진행한다.
# 맨 끝 일정부터 이 일정이 선택될 수 있는 조건은 다음과 같다.
# 현재 까지의 일정과 선택할 일정의 합이 7일보다 작거나 같다.
# 선택할 일정이 조건과 맞다면, 선택할 일정의 pay값과 현재 dp값에서
# 선택할 일정의 합의 dp값의 합과 전의 dp 값과 비교해서 큰 값을 값으로 저장한다.
# 이렇게 되면 dp0 항에 최댓값이 저장되게 된다.
N = int(input())
schedule_list = []
for _ in range(N):
    day, pay = map(int, input().split())
    schedule_list.append([day, pay])
dp_list = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    present_day = schedule_list[i][0]
    present_pay = schedule_list[i][1]
    if present_day + i > N:
        dp_list[i] = dp_list[i + 1]
    else:
        dp_list[i] = max(dp_list[i + 1], present_pay + dp_list[i + present_day])
print(dp_list[0])