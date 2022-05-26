for T in range(int(input())):
    S = input().rstrip()
    answer = []
    for i in S:
        if i == 'b':
            answer.append('d')
        elif i == 'd':
            answer.append('b')
        elif i == 'p':
            answer.append('q')
        else:
            answer.append('p')
    answer.reverse()
    print("#{} {}".format(T + 1, ''.join(answer)))
