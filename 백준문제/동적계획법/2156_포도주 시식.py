# dp_list[i]는 i번째 포도주 잔을 선택하였을때의 가장 많은 포도주의
# 값이다. 효주가 i번째 포도주를 선택할 수 있으려면,
# 연속으로 3잔을 선택할 수 없기 때문에, i-2, i-1번째 중 둘 중 하나를
# 선택한 결과값이 큰 것을 저장한다.
# 따라서 점화식 ai = max(ai-3 + i-1번째 포도주의 양, ai-2) + i 번째 포도주의 양
# 그러나 이 방법은 틀렸다...
# 현재의 포도주를 선택하지 않고도 최대의 포도주의 양을 구할 수 있는
# 경우가 있기 때문이다. 따라서 현재의 와인을 선택하지 않을 수 있는 i - 1번째
# 까지의 와인을 선택한 경우도 추가해서 큰 것을 저장해준다.
n = int(input())
wine_list = [0]
for i in range(n):
    wine_list.append(int(input()))
dp = [0]
dp.append(wine_list[1])
if n > 1:
    dp.append(wine_list[1] + wine_list[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + wine_list[i - 1] + wine_list[i], dp[i - 2] + wine_list[i]))
print(dp[n])
