# dp_list[i]는 i의 비용을 처음 넘는 최대의 고객 수를
# 나타낸다.
# 앞서서 풀었던 효율적인 화폐 구성과 동일하게 풀 수 있는 문제다.
C, N = map(int, input().split())
city_list = []
for _ in range(N):
    pay, customer = map(int, input().split())
    city_list.append([pay, customer])
city_list.sort(key=lambda x: x[1])
dp_list = [0] * (100 * 1000 + 1)
for i in range(N):
    for j in range(city_list[i][0], 100 * 1000 + 1):
        dp_list[j] = max(dp_list[j], dp_list[j - city_list[i][0]] + city_list[i][1])
for i in range(100 * 1000 + 1):
    if dp_list[i] >= C:
        print(i)
        break
