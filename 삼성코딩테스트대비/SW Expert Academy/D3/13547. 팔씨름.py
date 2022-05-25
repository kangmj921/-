for T in range(int(input())):
    S = input().rstrip()
    s_win, o_win = 0, 0
    for i in range(len(S)):
        if S[i] == 'o':
            s_win += 1
        else:
            o_win += 1
    if s_win >= 8 or o_win < 8:
        answer = "YES"
    else:
        answer = 'NO'
    print("#{} {}".format(T + 1, answer))
