for T in range(int(input())):
    S = input()
    answer = "Exist"
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - 1 - i]:
            if S[i] == '*' or S[len(S) - 1 - i] == '*':
                answer = "Exist"
                break
            answer = "Not exist"
            break
    print("#{} {}".format(T + 1, answer))
