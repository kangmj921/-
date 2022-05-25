for T in range(int(input())):
    N = int(input())
    answer = 'impossible'
    check = False
    for i in range(2, 10):
        k_N = list(str(i * N))
        if check:
            break
        temp = list(str(N))
        for j in list(str(N)):
            if j in k_N:
                temp.remove(j)
                k_N.remove(j)
        if not k_N:
            answer = 'possible'
            check = True
    print("#{} {}".format(T + 1, answer))
