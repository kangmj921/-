for T in range(int(input())):
    D, L, N = map(int, input().split())
    answer = 0
    for i in range(1, N + 1):
        answer += D * (1 + (i - 1) * (L / 100))
    print("#{} {}".format(T + 1, int(answer)))
