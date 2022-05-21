for T in range(int(input())):
    A, B, C, D = map(int, input().split())
    ALICE, BOB = A/B, C/D
    if ALICE > BOB:
        answer = 'ALICE'
    elif ALICE == BOB:
        answer = 'DRAW'
    else:
        answer = 'BOB'
    print("#{} {}".format(T + 1, answer))
