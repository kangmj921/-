# 점화식 생각이 잘 안난다.
N = int(input())
schedule_list = []
for _ in range(N):
    schedule_list.append(list(map(int, input().split())))
dp_list = [[0, 0] for _ in range(N)]
dp_list[0] = schedule_list[0]
for i in range(N):
    j = i + schedule_list[i][0]
    while j < N:
        dp_list[j][1] = max(dp_list[j][1], dp_list[i][1] + schedule_list[j][1])
        if dp_list[j][1] > dp_list[i][1] + schedule_list[j][1]:
            j += dp_list[j][0]
        else:
            j += dp_list[i][0] + schedule_list[j][0]
print(dp_list)
