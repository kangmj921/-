# DP를 사용하는 Knapsack 알고리즘의 대표격 문제이다.
# i번째 물건이 배낭의 부피 한도보다 많다면 넣을 수 없으므로 i번째 물건을 뺀
# i - 1개의 물건들을 가지고 구한 전 단계의 값을 가져온다.

# 그렇지 않은 경우, i번째 물건을 위해 i번째 물건만큼의 부피를 비웠을 때의 최적값에 i번째
# 물건의 가치를 더한 값 or i - 1개의 물건들을 가지고 구한 전 단계의 값 중 큰 값을 선택한다.
for T in range(int(input())):
    N, K = map(int, input().split())
    item_list = [[0, 0]]
    answer = 0
    dp_list = [[0] * (K + 1) for _ in range(N + 1)]
    for _ in range(N):
        item_list.append(list(map(int, input().split())))
    for i in range(1, N + 1):
        for w in range(1, K + 1):
            if item_list[i][0] > w:
                dp_list[i][w] = dp_list[i - 1][w]
            else:
                dp_list[i][w] = max(item_list[i][1] + dp_list[i - 1][w - item_list[i][0]], dp_list[i - 1][w])
    answer = dp_list[N][K]
    print("#{} {}".format(T + 1, answer))
