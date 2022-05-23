for TC in range(int(input())):
    S = input()
    answer = 'Yes'
    for i in S:
        if S.count(i) != 2:
            answer = 'No'
            break
    print("#{} {}".format(TC + 1, answer))
