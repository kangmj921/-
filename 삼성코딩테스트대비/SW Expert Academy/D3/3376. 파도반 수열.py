def P(N):
    stack = [0, 1, 1, 1, 2, 2, 3, 4, 5]
    if N >= len(stack):
        index = 8
        n = 4
        while index < N:
            stack.append(stack[-1] + stack[n])
            index += 1
            n += 1
    return stack[N]


for T in range(int(input())):
    print("#{} {}".format(T + 1, P(int(input()))))
