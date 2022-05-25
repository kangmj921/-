for T in range(int(input())):
    P = input().rstrip()
    Q = input().rstrip()
    if P + 'a' != Q:
        answer = 'Y'
    else:
        answer = 'N'
    print("#{} {}".format(T + 1, answer))