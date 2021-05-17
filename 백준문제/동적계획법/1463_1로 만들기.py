# 2부터 N까지 모든 수에 대해서, 연산 수의 값은 3으로 나눈 수의 연산수
# +1 와의 최솟값이거나, 2로 나눈 수의 연산수 + 1 와의 최솟값 또는
# 1로 뺀 수의 연산수와의 최솟값으로 나타낼 수 있다.
N = int(input())
num_list = [1e9] * (N + 1)
num_list[1] = 0
for i in range(2, N + 1):
    if i % 3 == 0:
        num_list[i] = min(num_list[i], num_list[i//3] + 1)
    if i % 2 == 0:
        num_list[i] = min(num_list[i], num_list[i//2] + 1)
    num_list[i] = min(num_list[i], num_list[i - 1] + 1)
print(num_list[N])
