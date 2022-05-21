for T in range(int(input())):
    D, H, M = map(int, input().split())
    answer = 0
    total_minute = M + H * 60 + D * 24 * 60
    today_minute = 11 + 11 * 60 + 11 * 24 * 60
    answer = total_minute - today_minute
    if answer < 0:
        answer = -1
    print("#{} {}".format(T + 1, answer))
