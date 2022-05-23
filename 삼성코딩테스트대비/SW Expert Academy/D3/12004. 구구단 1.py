for TC in range(int(input())):
    N = int(input())
    answer = "NO"
    check = False
    for i in range(1, 10):
        if not check:
            for j in range(i, 10):
                if i * j == N:
                    answer = "YES"
                    check = True
                    break
    print("#{} {}".format(TC + 1, answer))
