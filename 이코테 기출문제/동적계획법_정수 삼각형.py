# 앞서 풀었던 금광 문제와 비슷한 방식으로 풀 수 있었다.
# 각 삼각형 경로의 수는 각 대각선 위의 수에서 구했던 경로들 중
# 최댓값을 찾아서 구할 수 있다.
# 점화식으로 나타내게 되면, ai,j = ni,j + max(ai-1,j, ai-1,j-1)
# 그리고 가장 끝 쪽에 존재해서 왼쪽 위 대각선이나 오른쪽 위 대각선에
# 밖에 수가 존재하지 않는 경우를 나눠서 예외처리 해주면 된다.
n = int(input())
num_list = [[] for _ in range(n)]
for i in range(n):
    num_list[i] = list(map(int, input().split()))
dp_list = [[0] * len(num_list[i]) for i in range(len(num_list))]
dp_list[0][0] = num_list[0][0]
for i in range(1, len(num_list)):
    for j in range(len(num_list[i])):
        if j == 0:
            dp_list[i][j] = num_list[i][j] + dp_list[i - 1][j]
        elif j == len(num_list[i]) - 1:
            dp_list[i][j] = num_list[i][j] + dp_list[i - 1][j - 1]
        else:
            dp_list[i][j] = num_list[i][j] + max(dp_list[i - 1][j - 1], dp_list[i - 1][j])
print(max(dp_list[-1]))
