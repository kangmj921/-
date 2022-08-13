# 돈의 수를 최소로 하려면
# 되도록 6개 패키지를 사고 6으로 나눈 나머지는 낱개로 산다.
# 따라서 6개 패키지를 고르는 기준은 6개 낱개를 살때 보다 가격이 같거나 쌀 때이다.
# 하지만 6개 보다 적은 낱개가 남았을 때, 낱개로 사는 거 보다 6개 패키지를 고를 때,
# 가격이 더 적다면 6개 패키지를 고른다.
# 그 외 상황은 그냥 낱개로 산다.
N, M = map(int, input().split())
brand_list = [list(map(int, input().split())) for _ in range(M)]
sort_by_n = sorted(brand_list, key=lambda x: x[1])
sort_by_6 = sorted(brand_list, key=lambda x: x[0])
# print(sort_by_n, sort_by_6)
answer = 0
if sort_by_6[0][0] <= sort_by_n[0][1] * 6:
    if sort_by_6[0][0] < sort_by_n[0][1] * (N % 6):
        answer = sort_by_6[0][0] * (N // 6 + 1)
    else:
        answer = sort_by_6[0][0] * (N // 6) + sort_by_n[0][1] * (N % 6)
else:
    answer += sort_by_n[0][1] * N
print(answer)
