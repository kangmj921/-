for T in range(int(input())):
    D, A, B, F = map(int, input().split())
    answer = F * D / (A + B)
    print("#{} {:.10f}".format(T + 1, answer))
