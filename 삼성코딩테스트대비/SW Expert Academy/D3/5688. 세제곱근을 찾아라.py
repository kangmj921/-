for T in range(int(input())):
    N = int(input())
    x = 1
    answer = 0
    while x ** 3 != N:
        if x ** 3 > N:
            answer = -1
            break
        x += 1
    if answer != -1:
        answer = x
    print("#{} {}".format(T + 1, answer))
