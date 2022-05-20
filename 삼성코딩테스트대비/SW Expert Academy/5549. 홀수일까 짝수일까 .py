for T in range(int(input())):
    N = int(input())
    if N % 2 == 0:
        print("#{} {}".format(T + 1, "Even"))
    else:
        print("#{} {}".format(T + 1, "Odd"))
