# N 을 입력받고 N 자리의 오르막 수의 개수를 구한다.
# dp 리스트를 N + 1 * N + 1 크기의 2차원으로 선언한다.
# dp[i][j]의 값은, j번째 자리수가 i일때 가지는 오르막 수의 값이다.
# 예를 들어, N이 1일때 dp의 값은,
# 0 1
# 0 1
# 0 1
# ...
# 0 1로 나타낼 수 있다. N이 2 이상일땐, 앞자리에
N = int(input())
dp_list = [[0] * (N + 1) for _ in range(11)]
answer = 0
for i in range(1, 11):
    dp_list[i][1] = 1  # N이 1일때에 대하여 dp 값 초기화
for i in range(2, N + 1):  # N이 2 이상일땐, 앞자리의 수에 따라 오르막 수의 개수가 결정된다.
    temp = sum(dp_list[k][i - 1] for k in range(1, 11))
    dp_list[1][i] = temp
    for j in range(2, 11):
        temp -= dp_list[j - 1][i - 1]
        dp_list[j][i] = temp
for i in range(1, 11):
    answer += dp_list[i][N]
print(answer % 10007)
