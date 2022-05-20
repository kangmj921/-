for T in range(int(input())):
    N, M, K = map(int, input().split())
    arrive_time = sorted(list(map(int, input().split())))
    answer = "Possible"
    for i in range(N):
        if arrive_time[i] < M:
            answer = "Impossible"
        else:
            total_bread = (arrive_time[i] // M) * K - i
            if not total_bread:
                answer = "Impossible"
    print("#{} {}".format(T + 1, answer))
