for T in range(int(input())):
    answer = 0
    start_day, total_day = 4, 0
    month_per_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m, d = map(int, input().split())
    for i in range(1, m):
        total_day += month_per_day[i]
    total_day += d - 1
    answer = (start_day + total_day % 7) % 7
    print("#{} {}".format(T + 1, answer))
