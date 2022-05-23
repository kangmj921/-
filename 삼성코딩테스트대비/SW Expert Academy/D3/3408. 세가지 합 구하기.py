for T in range(int(input())):
    N = int(input())
    answer1, answer2, answer3 = 0, 0, 0
    answer1 = N * (N + 1) // 2
    answer2 = N * (2 + 2 * (N - 1)) // 2
    answer3 = N * (4 + 2 * (N - 1)) // 2
    print("#{} {} {} {}".format(T + 1, answer1, answer2, answer3))
