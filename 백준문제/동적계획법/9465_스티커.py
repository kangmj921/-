# 현재의 스티커가 선택되기 위해서는, 현재의 스티커 점수가
# 훼손되는 스티커 점수보다 클 경우이거나, 아니면 지금까지 선택된
# 스티커들이 선택할 스티커와 한 변을 공유하지 않는 경우이다.
# 점화식은 좀 더 고민해야될 듯.
for _ in range(int(input())):
    n = int(input())
    sticker_list = [list(map(int, input().split())), list(map(int, input().split()))]
    dp_list = [[0] * n for _ in range(2)]
    for i in range(2):
        for j in range(n):
            dp_list[i][j] = max()