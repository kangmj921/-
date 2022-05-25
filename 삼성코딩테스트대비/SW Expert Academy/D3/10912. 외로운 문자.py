for T in range(int(input())):
    string = list(input().rstrip())
    string.sort()
    stack = []
    for i in range(len(string)):
        if len(stack) != 0 and string[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(string[i])
    if len(stack) == 0:
        answer = 'Good'
    else:
        answer = ''.join(stack)
    print("#{} {}".format(T + 1, answer))
