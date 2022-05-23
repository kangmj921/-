for T in range(int(input())):
    N, A, B = map(int, input().split())
    min_ = (A + B) - N
    if min_ < 0:
        min_ = 0
    max_ = min(A, B)
    print("#{} {} {}".format(T + 1, max_, min_))
