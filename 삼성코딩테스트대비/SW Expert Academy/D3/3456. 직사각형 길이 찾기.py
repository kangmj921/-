for T in range(int(input())):
    answer = 0
    a, b, c = map(int, input().split())
    if a == b:
        answer = c
    elif a == c:
        answer = b
    else:
        answer = a
    print("#{} {}".format(T + 1, answer))
