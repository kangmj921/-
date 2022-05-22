for T in range(int(input())):
    N = int(input())
    n_list = list(map(int, input().split()))
    dp_list = [0] * N
    dp_list[0] = n_list[0]
    check_minus = max(n_list)
    if check_minus < 0:
        answer = check_minus
    else:
        for i in range(1, len(dp_list)):
            dp_list[i] = max(dp_list[i - 1] + n_list[i], dp_list[i])
        answer = max(dp_list)
    print("#{} {}".format(T + 1, answer))
