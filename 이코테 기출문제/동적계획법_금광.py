# 각 금광에서 얻을 수 있는 최대 값은 이동하기 전에 얻을 수 있는 금광의 값 최대값과 현재 금광의 값의
# 합과 같다. 첫 열의 어떤 행에서도 출발할 수 있으므로, 각 행에서 출발한 값의 최댓값을 살펴보기 위해
# for문을 돌릴때 가로 먼저 그리고 세로 먼저 해야 답이 나온다.
for _ in range(int(input())):
    n, m = map(int, input().split())
    input_list = list(map(int, input().split()))
    mine_list = [input_list[i:i+m] for i in range(0, n*m, m)]
    for j in range(1, m):
        for i in range(n):
            if 0 < i < n - 1:
                mine_list[i][j] += max(mine_list[i][j - 1], mine_list[i - 1][j - 1], mine_list[i + 1][j - 1])
            elif i == n - 1:
                mine_list[i][j] += max(mine_list[i][j - 1], mine_list[i - 1][j - 1])
            elif i == 0:
                mine_list[i][j] += max(mine_list[i][j - 1], mine_list[i + 1][j - 1])
    result = 0
    for i in range(n):
        result = max(result, mine_list[i][m - 1])
    print(result)
