# 왼쪽부터 차례대로 식량창고를 턴다고 가정했을 때, 왼쪽부터 차례대로
# 식량창고를 털지 안 털지를 결정하는 경우와 특정한 i번째 식량 창고에 대해
# 털지 안 털지 여부를 결정할 때, 단 2가지 경우만 확인하면 된다.
# 첫 번째, i - 1 번째 식량창고를 털기로 한 경우, i 번째 식량창고는 털 수 없다.
# 두 번째, i - 2 번째 식량창고를 털기로 한 경우, i 번째 식량창고를 털 수 있다.
# 따라서 위 2가지 경우 중에서, 더 많은 식량을 털 수 있는 경우를 선택하면 된다.
# 주의할 점은, i - 3 번째 이하의 식량창고에 대해서는 고려할 필요가 없다.
# 왜냐하면 한 칸 이상 떨어진 식량창고는 항상 털 수 있기 때문이다.
N = int(input())
store_list = list(map(int, input().split()))
stolen_amount = [0] * N
stolen_amount[0] = store_list[0]
stolen_amount[1] = max(store_list[1], store_list[0])
for j in range(2, N):
    stolen_amount[j] = max(stolen_amount[j - 1], stolen_amount[j - 2] + store_list[j])
print(stolen_amount[N - 1])
