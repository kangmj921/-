for T in range(int(input())):
    A, B, C = map(int, input().split())
    answer = 0
    if A >= B:
        answer += C // B
    else:
        answer += C // A
    print("#{} {}".format(T + 1, answer))
