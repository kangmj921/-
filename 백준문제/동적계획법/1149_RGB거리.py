# dp에 저장되는 값은 i번째 집이 j번째 색을 선택했을때 얻을 수 있는 최소의 비용이다.
# 각 집은 인접한 집과 색깔이 같지 않아야 하므로,
# dp의 값을 초기화해나갈때, 이전의 집의 색과 다른 색으로 칠하면서 진행한다.
# 따라서 dp[i][j]는 price[i][j] + min(양 옆의 집을 j와 다른 색으로 칠할때 저장된 값)
# 결국 최종적으로 비용의 최솟값은 마지막 집을 칠할때
# dp[N][j] 중 최솟값을 구하면 된다.
import sys


if __name__ == "__main__":
    num_house = int(input())
    price = [list(map(int, sys.stdin.readline().split())) for _ in range(num_house)]
    dp_list = [[0] * 3 for _ in range(num_house)]
    dp_list[0] = price[0]
    for i in range(1, num_house):
        dp_list[i][0] = price[i][0] + min(dp_list[i - 1][1], dp_list[i - 1][2])
        dp_list[i][1] = price[i][1] + min(dp_list[i - 1][0], dp_list[i - 1][2])
        dp_list[i][2] = price[i][2] + min(dp_list[i - 1][1], dp_list[i - 1][0])
    print(min(dp_list[num_house - 1]))
