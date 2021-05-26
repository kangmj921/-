# 각 자리수에 대해, 제일 첫 자리에 올 수 있는 수는 1~9
# 그 다음 자리 부터는 0~9까지의 수가 올 수 있다.
# 이중 전 자리 수가 0이나 9인 경우에 뒤에 수는
# 1이나 8로 각각 한 가지 경우이고, 나머지 수들은
# 자기 보다 1 크고 작은 수가 올 수 있는 2가지 경우이다.
# 따라서 dp_list[i]는 i번째 자리수에 0~9가 몇 번 나오는지 저장한다.
# 현재 자리수에 0이나 9는 전 자리수에 1과 8이 나오는 수와 같고
# 나머지 수는 전 자리수에 자신보다 1크고 작은 수가 나온 횟수를 더한
# 값이 된다.
N = int(input())
dp_list = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp_list[1][i] = 1
for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp_list[i][j] = dp_list[i - 1][j + 1]
        elif j == 9:
            dp_list[i][j] = dp_list[i - 1][j - 1]
        else:
            dp_list[i][j] = dp_list[i - 1][j - 1] + dp_list[i - 1][j + 1]
print(sum(dp_list[N]) % 1000000000)
