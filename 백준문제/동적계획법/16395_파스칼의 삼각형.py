n, k = map(int, input().split())
dp_list = [[0]]
for i in range(1, n + 1):
    dp_list.append([1] * i)
    if i > 2:
        for j in range(1, i - 1):
            dp_list[i][j] = dp_list[i - 1][j] + dp_list[i - 1][j - 1]
print(dp_list[n][k - 1])
