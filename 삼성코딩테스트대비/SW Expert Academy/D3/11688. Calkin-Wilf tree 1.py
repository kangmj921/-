for T in range(int(input())):
    S = input().rstrip()
    Root = [1, 1]
    for i in S:
        if i == 'L':
            Root[0], Root[1] = Root[0], Root[0] + Root[1]
        else:
            Root[0], Root[1] = Root[0] + Root[1], Root[1]
    print("#{} {} {}".format(T + 1, Root[0], Root[1]))
