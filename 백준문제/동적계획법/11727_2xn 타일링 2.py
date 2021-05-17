# 앞선 문제 2 x n 타일링 문제에서 2 x 2 타일이 추가되었다.
# 이렇게 되면, 2 x n - 1 번째 타일까지 채워졌을때 추가하는 경우의
# 수는 같지만, 2 x n - 2 번째 타일까지 채워졌을때 추가하는 경우가
# 2 x 1 타일 2개, 그리고 2 x 2 타일 1개를 추가하는 경우로 2가지가 된다.
# 따라서 점화식으로 나타내게 되면, ai = ai-1 + 2*ai-2이다.
n = int(input())
num_list = [0] * 1001
num_list[1], num_list[2] = 1, 3
for i in range(3, n + 1):
    num_list[i] = num_list[i - 1] + num_list[i - 2] * 2
print(num_list[n] % 10007)
