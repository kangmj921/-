for TC in range(int(input())):
    A, B = map(int, input().split())
    answer = 0
    if A >= 10 or B >= 10:
        answer = -1
    else:
        answer = A * B
    print("#{} {}".format(TC + 1, answer))
