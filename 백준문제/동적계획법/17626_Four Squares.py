# 각 항의 값은 우선, ai = 1 + ai-1 로 나타낼 수 있으며,
# ai의 값을 최소화 하기 위해서는 더해지는 제곱수 중 가장 큰 값을
# 구해야함.
N = int(input())
num_list = [0, 1]
for i in range(2, N + 1):
    min_value = 1e9
    j = 1
    while j ** 2 <= i:
        min_value = min(min_value, num_list[i - (j**2)])
        j += 1
    num_list.append(min_value + 1)
print(num_list[N])
