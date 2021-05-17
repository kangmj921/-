# 마지막 계단은 꼭 밟아야 하므로, 마지막 계단의 전 계단을 밟은 경우와
# 밟지 않은 경우로 나눌 수 있다.
# 마지막 계단의 전 계단을 밟은 경우, 3개의 계단을 연속해서 밟을 수 없으므로
# 마지막 계단 - 3 번째 까지의 결과에 마지막계단과 마지막계단의 전 계단의 값의 합이다.
# 마지막 계단의 전 계단을 밟지 않은 경우, 마지막 계단 - 2 번쨰 까지의 결과와
# 마지막 계단의 합이다. 이 중 큰 값을 결과 값으로 넣어준다.
N = int(input())
stair_list = [0] * 301
for i in range(N):
    stair_list[i] = int(input())
result = [0] * 301
result[0] = stair_list[0]
result[1] = stair_list[0] + stair_list[1]
result[2] = max(stair_list[0] + stair_list[2], stair_list[1] + stair_list[2])
for i in range(3, N):
    result[i] = max(result[i-2] + stair_list[i], result[i - 3] + stair_list[i - 1] + stair_list[i])
print(result[N - 1])
