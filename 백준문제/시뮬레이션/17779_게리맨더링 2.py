def divide_election_district(x, y, d1, d2):
    cal = [0 for i in range(6)]
    temp = [[0] * (N + 1) for i in range(N + 1)]
    for i in range(d1 + 1):
        temp[x + i][y - i] = 5
        temp[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        temp[x + i][y + i] = 5
        temp[x + d1 + i][y - d1 + i] = 5
    for i in range(x + 1, x + d1 + d2):
        check = False
        for j in range(1, N + 1):
            if temp[i][j] == 5:
                check = not check
            if check:
                temp[i][j] = 5
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if r < x + d1 and c <= y and temp[r][c] == 0:
                cal[1] += A_list[r][c]
            elif r <= x + d2 and y < c and temp[r][c] == 0:
                cal[2] += A_list[r][c]
            elif x + d1 <= r and c < y - d1 + d2 and temp[r][c] == 0:
                cal[3] += A_list[r][c]
            elif x + d2 < r and y - d1 + d2 <= c and temp[r][c] == 0:
                cal[4] += A_list[r][c]
            elif temp[r][c] == 5:
                cal[5] += A_list[r][c]
    return max(cal[1:]) - min(cal[1:])


N = int(input())
# 5 <= N <= 20
A_list = [[]]
for _ in range(N):
    A_list.append([0] + list(map(int, input().split())))
# 1 <= A[r][c] <= 100
answer = 10 ** 9
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):  # 여기까지 최대 20^4 = 160000의 시간 복잡도.
                if 1 <= x < x + d1 + d2 <= N and 1 <= y - d1 < y < y + d2 <= N:
                    answer = min(answer, divide_election_district(x, y, d1, d2))
print(answer)
