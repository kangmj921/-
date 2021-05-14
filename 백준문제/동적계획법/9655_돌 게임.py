# 돌이 3개, 1개 있을때 소비되는 턴은 1이고, 돌이 2개 있을 때 부터 소비되는
# 턴은 돌을 1개 빼기 전이나 3개 빼기 전에 소요된 턴에서 1턴 더 소비된 것이다.
# 따라서 이를 점화식으로 표현하게 되면,
# ai = min(ai-3, ai-1) + 1 로 나타낼 수 있다.
N = int(input())
turn_list = [1e9] * 1001
turn_list[1] = 1
turn_list[3] = 1
for i in range(2, N + 1):
    if i >= 3:
        turn_list[i] = min(turn_list[i], turn_list[i - 3] + 1)
    if i >= 1:
        turn_list[i] = min(turn_list[i], turn_list[i - 1] + 1)
if turn_list[N] % 2 != 0:
    print('SK')
else:
    print("CY")
