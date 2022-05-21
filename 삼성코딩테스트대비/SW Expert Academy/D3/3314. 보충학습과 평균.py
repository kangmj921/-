for T in range(int(input())):
    score_list = list(map(int, input().split()))
    total = 0
    for i in score_list:
        if i < 40:
            total += 40
        else:
            total += i
    print("#{} {}".format(T + 1, total // 5))
