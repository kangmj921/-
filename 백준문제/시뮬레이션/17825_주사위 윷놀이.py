# 모든 주사위에서 나온 수를 말 1개가 이동했을때 부터 시작해서
# 모든 주사위에서 나온 수를 말 4개가 이동했을때 까지 경우를 브루트포스로 구하면서
# 최대 점수를 계산한다.
# 이때 칸 수가 각 score_list 의 길이 보다 큰 경우 도착을 이미 한 것이다.

# 4개의 말을 10번 이동시키는 경우의 수는, 4 ^ 10 = 1048576
def dfs(marker_cord, dice, idx, score):
    if idx == 10:
        global answer
        answer = max(score, answer)
        return
    for i in range(4):
        if marker_cord[i][0] == -1:
            continue
        marker_cord[i][1] += dice[idx]
        my, mx = marker_cord[i][0], marker_cord[i][1]

        if mx >= len(score_list[my]):
            marker_cord[i][0] = -1
            dfs(marker_cord, dice, idx + 1, score)
            marker_cord[i][0] = my
            marker_cord[i][1] -= dice[idx]
        else:
            if not my and not score_list[my][mx] % 10 and score_list[my][mx] != 40:
                marker_cord[i][0] += score_list[my][mx] // 10
            check_marker_same = False
            for j in range(4):
                if j == i:
                    continue
                ny, nx = marker_cord[j][0], marker_cord[j][1]
                if ny == -1:
                    continue
                if (my and ny) and ((nx == mx and score_list[ny][nx] == 30 and score_list[my][mx] == 30) or (
                        score_list[ny][nx] == 35 and score_list[my][mx] == 35)):
                    check_marker_same = True
                    break
                if marker_cord[j] == marker_cord[i] or (score_list[ny][nx] == 25 and score_list[my][mx] == 25) or (
                        score_list[ny][nx] == 40 and score_list[my][mx] == 40):
                    check_marker_same = True
                    break
            if check_marker_same:
                marker_cord[i][0] = my
                marker_cord[i][1] -= dice[idx]
                continue
            dfs(marker_cord, dice, idx + 1, score + score_list[marker_cord[i][0]][marker_cord[i][1]])
            marker_cord[i][0], marker_cord[i][1] = my, mx - dice[idx]
        if idx == i:
            break


dice_list = list(map(int, input().split()))
score_list = [[i for i in range(0, 42, 2)],
              [i for i in range(0, 12, 2)] + [13, 16, 19] + [i for i in range(25, 45, 5)],
               [i for i in range(0, 26, 2)] + [i for i in range(25, 45, 5)],
              [i for i in range(0, 32, 2)] + [28, 27, 26] + [i for i in range(25, 45, 5)]]
answer = 0
marker = [[0, 0] for _ in range(4)]
dfs(marker, dice_list, 0, 0)
print(answer)
