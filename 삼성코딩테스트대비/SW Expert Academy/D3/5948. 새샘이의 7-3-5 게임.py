for T in range(int(input())):
    num_list = list(map(int, input().split()))
    stack = []
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            for k in range(j + 1, len(num_list)):
                stack.append(num_list[i] + num_list[j] + num_list[k])
                stack = set(stack)
                stack = list(stack)
    print("#{} {}".format(T + 1, sorted(stack, reverse=True)[4]))
