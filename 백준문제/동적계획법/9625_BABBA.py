K = int(input())
dp_list = [[0, 0] for _ in range(K + 1)]
dp_list[1] = [0, 1]
for i in range(2, K + 1):
    dp_list[i][0] = dp_list[i - 1][1]
    dp_list[i][1] = dp_list[i - 1][1] + dp_list[i - 1][0]
print(*dp_list[K])
