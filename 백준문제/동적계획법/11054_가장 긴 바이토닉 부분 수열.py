# 바이토닉 부분 수열은 증가하는 부분 수열로 이루어지다가 감소하는 부분 수열로 이루어진 순열이다.
# 증가하는 부분 수열을 구하는 부분은 지난번에 푼 문제에서와 똑같이 구하면 되지만,
# 감소하는 부분을 구하는 것은, 제일 끝 부분에서 시작해서 시작 부분으로 오는 역방향 증가하는 부분 수열을 구하는 식으로
# 그리고 결과적으로 증가 순열 값 + 역방향 증가 순열 값  -1 (겹치는 i번째 수) 를 하면 결과를 구할 수 있다.
N = int(input())
A_list = [0] + list(map(int, input().split()))
dp_list_increase = [0] * (N + 1)
dp_list_decrease = [0] * (N + 1)
for i in range(1, N + 1):
    dp_list_increase[i] = 1
    for j in range(i):
        if A_list[j] < A_list[i]:
            dp_list_increase[i] = max(dp_list_increase[i], dp_list_increase[j] + 1)
for k in range(N, 0, -1):
    dp_list_decrease[k] = 1
    for j in range(N, k - 1, -1):
        if A_list[j] < A_list[k]:
            dp_list_decrease[k] = max(dp_list_decrease[k], dp_list_decrease[j] + 1)
# print(dp_list_increase, dp_list_decrease)
result = [0] * (N + 1)
for i in range(1, N + 1):
    result[i] = dp_list_increase[i] + dp_list_decrease[i] - 1
print(max(result))
