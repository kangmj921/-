# 유명한 알고리즘은 냅색 알고리즘을 사용하는 문제.
# 한 물건은 선택하는 조건은, 지금까지 고른 물건들의 무게 합이 K에서 지금 고른 물건의 무게를 뺀 값과
# 같거나 더 작을때이다.
# 물건을 선택할때, 선택하지 않을때 2가지 경우를 취합하여 최댓 가치를 가지는 경우를 dp에 저장한다.
#

# 기존에 냈던 코드는 물건을 N개 모두 넣고, 2차원의 dp에서 N번째 물건까지의 선택에 따른 가치의 최댓값을 구했는데
# 그렇게 하기 보다 물건을 입력 받는 과정이 N번째 까지의 물건을 고르는 과정과 똑같으므로
# 입력과 동시에 dp 값을 처리하는 코드가 훨씬 실행시간이 빨랐다.
#

N, K = map(int, input().split())
dp_list = [0] * (K + 1)
for _ in range(N):
    W, V = map(int, input().split())
    for j in range(K, W - 1, -1):
        dp_list[j] = max(dp_list[j], dp_list[j - W] + V)
# 기존에 작성했던 코드
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         if item_list[i][0] > j:
#             # i번째 물건이 무게 제한보다 크므로, i - 1 번째 물건을 선택했을때까지의 최적값을 가져온다.
#             dp_list[i][j] = dp_list[i - 1][j]
#         else:
#             # i번째 물건을 위해 i번째 물건만큼의 부피를 비웠을 때의 최적값에
#             # i번째 물건의 가치를 더한 값 or i - 1개의 물건들을 가지고 구한 전 단계의 값 중 큰 값을 선택한다.
#             dp_list[i][j] = max(dp_list[i - 1][j - item_list[i][0]] + item_list[i][1], dp_list[i - 1][j])
print(dp_list[K])
