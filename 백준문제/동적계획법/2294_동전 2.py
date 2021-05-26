# 앞서 풀었던 효율적인 화폐 구성과 동일한 문제이다.
n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
coin_list.sort()
dp_list = [100000] * (k + 1)
dp_list[0] = 0
for i in coin_list:
    for j in range(i, k + 1):
        if dp_list[j - i] != 100000:
            dp_list[j] = min(dp_list[j - i] + 1, dp_list[j])
if dp_list[k] == 100000:
    print(-1)
else:
    print(dp_list[k])
