for T in range(int(input())):
    s = input().rstrip('\n')
    decorated = [['.'] * (len(s) * 5 - (len(s) - 1)) for _ in range(5)]
    for i in range(2):
        for j in range(len(decorated[i])):
            if i % 2 == 1 and j % 2 == 1:
                decorated[i][j] = '#'
                decorated[4 - i][j] = '#'
            if i % 2 == 0 and j % 4 == 2:
                decorated[i][j] = '#'
                decorated[4 - i][j] = '#'
    index = 0
    for i in range(len(decorated[2])):
        if i % 4 == 2:
            decorated[2][i] = s[index]
            index += 1
        elif i % 4 == 0:
            decorated[2][i] = '#'
    for i in range(5):
        print("".join(decorated[i]))
