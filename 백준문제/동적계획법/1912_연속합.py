# 연속합을 저장하는 dp의 값은, 현재까지 저장된 dp의 값과
# 그 전 항까지 저장된 dp의 값, 현재 항의 수의 합 중 큰 것으로
# 저장한다.
# 점화식으로 나타내게 된다면, ai = max(ai, ai-1 + ni)
# 그렇게 구해진 각 dp값은 해당 인덱스 까지의 연속합의 최댓값들을
# 나타내게 되는데, 여기서 dp의 최댓값이 0인 경우는 모든 수가 음수인
# 경우이므로, 이때는 원래 배열에서 제일 큰 수 하나만 선택했을때
# 최대의 연속합을 가지게 된다.
N = int(input())
num_list = list(map(int, input().split()))
dp_list = [0] * N
dp_list[0] = num_list[0]
for i in range(1, N):
    dp_list[i] = max(dp_list[i], dp_list[i - 1] + num_list[i])
result = max(dp_list)
if result == 0:
    print(max(num_list))
else:
    print(result)
