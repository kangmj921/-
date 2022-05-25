for T in range(int(input())):
    A, B = map(int, input().split())
    answer = (A + B) % 24
    print("#{} {}".format(T + 1, answer))
