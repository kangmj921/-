for T in range(int(input())):
    string = list(input())
    H = int(input())
    hypen_index = list(map(int, input().split()))
    for i in range(len(hypen_index)):
        j, c = 0, 0
        while j < len(string):
            if hypen_index[i] == 0:
                string.insert(0, '-')
                break
            if string[j] != '-':
                c += 1
            if c == hypen_index[i]:
                string.insert(j + 1, '-')
                break
            j += 1
    print("#{}".format(T + 1), "".join(string))
