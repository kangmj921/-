# 적은 금액부터 큰 금액까지 차례대로 확인하며 만들 수 있는
# 최소한의 화폐 개수를 찾는다.
# 금액 i를 만드는 최소한 화폐 개수를 ai라고 할때, 화폐 단위가 k일때
# ai-k가 존재한다면, ai = min(ai, ai-k + 1)이고
# 존재하지 않는다면, 초기화되었던 10001 그대로이다.
N, M = map(int, input().split())
coin_list = []
result = [10001] * (M + 1)
result[0] = 0
for _ in range(N):
    coin_list.append(int(input()))
coin_list.sort()
for i in range(N):
    for j in range(coin_list[i], M + 1):
        if result[j - coin_list[i]] != 10001:
            result[j] = min(result[j], result[j - coin_list[i]] + 1)
if result[M] == 10001:
    print(-1)
else:
    print(result[M])
