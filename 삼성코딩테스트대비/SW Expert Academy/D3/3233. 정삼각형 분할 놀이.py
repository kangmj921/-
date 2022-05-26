for T in range(int(input())):
    A, B = map(int, input().split())
    answer = 1
    if A != B:
        for i in range(1, A // B):
            answer += 2 * i + 1
    print("#{} {}".format(T + 1, answer))
