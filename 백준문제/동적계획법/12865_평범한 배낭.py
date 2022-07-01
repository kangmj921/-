# 유명한 알고리즘은 냅색 알고리즘을 사용하는 문제.
# 한 물건은 선택하는 조건은, 지금까지 고른 물건들의 무게 합이 K에서 지금 고른 물건의 무게를 뺀 값과
# 같거나 더 작을때이다.
# 물건을 선택할때, 선택하지 않을때 2가지 경우를 취합하여 최댓 가치를 가지는 경우를 dp에 저장한다.
#

N, K = map(int, input().split())
item_list = [[0]]
dp_list = [[0] * (1000000 + 1) for _ in range(N + 1)]
for _ in range(N):
    W, V = map(int, input().split())
    dp_list[1][W] = V
    item_list.append([W, V])
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if item_list[i][0] > j:
            # i번째 물건이 무게 제한보다 크므로, i - 1 번째 물건을 선택했을때까지의 최적값을 가져온다.
            dp_list[i][j] = dp_list[i - 1][j]
        else:
            # i번째 물건을 위해 i번째 물건만큼의 부피를 비웠을 때의 최적값에
            # i번째 물건의 가치를 더한 값 or i - 1개의 물건들을 가지고 구한 전 단계의 값 중 큰 값을 선택한다.
            dp_list[i][j] = max(dp_list[i - 1][j - item_list[i][0]] + item_list[i][1], dp_list[i - 1][j])
print(dp_list[N][K])
