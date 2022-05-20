for T in range(int(input())):
    L, U, X = map(int, input().split())
    answer = 0
    if X > U:
        answer = -1
    else:
        if X >= L:
            answer = 0
        else:
            answer = L - X
    print("#{} {}".format(T + 1, answer))
