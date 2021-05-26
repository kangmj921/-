# k원의 가치를 만드는 경우의 수는,
# k원에서 동전을 하나씩 뺀 가치의 경우의 수들의 합과 같다.
# 예를 들어 동전 1, 2, 5가 있을 경우, k원의 가치는
# k - 1, k - 2, k - 5 가치의 경우의 수들의 합과 같다.
# 이 때 이 가치들은 0보다 작아서는 안된다.
n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
coin_list.sort()
dp_list = [0] * (k + 1)
dp_list[0] = 1
for i in coin_list:
    for j in range(i, k + 1):
        if j - i >= 0:
            dp_list[j] += dp_list[j - i]
print(dp_list[k])
