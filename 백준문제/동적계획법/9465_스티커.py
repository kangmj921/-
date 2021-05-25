# dp_list[i][j]는 i열의 j 행 스티커를 선택하였을 때 얻을 수 있는 최대 점수를 저장한다.
# 현재의 스티커가 선택되기 위해서는, 대각선에 위치한 스티커를 선택하였거나
# 한 변을 공유하고 있지 않은 스티커를 선택하였을 경우이다.
# 이 중 최대 점수를 얻을 수 있는 값을 선택하고 현재의 스티커 값을 더해서 저장한다.
for _ in range(int(input())):
    n = int(input())
    sticker_list = [list(map(int, input().split())), list(map(int, input().split()))]
    dp_list = [[0] * n for _ in range(2)]
    dp_list[0][0] = sticker_list[0][0]
    dp_list[0][1] = sticker_list[0][1] + sticker_list[1][0]
    dp_list[1][0] = sticker_list[1][0]
    dp_list[1][1] = sticker_list[1][1] + sticker_list[0][0]
    for i in range(2, n):
        dp_list[0][i] = sticker_list[0][i] + max(dp_list[1][i - 1], dp_list[1][i - 2])
        dp_list[1][i] = sticker_list[1][i] + max(dp_list[0][i - 1], dp_list[0][i - 2])
    print(max(dp_list[0][n-1], dp_list[1][n-1]))
