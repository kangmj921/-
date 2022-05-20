def check(n):
    stack = [int(n[0])]
    for i in range(1, len(n)):
        if int(n[i]) < stack[-1]:
            return False
        stack.append(int(n[i]))
    return True


for T in range(int(input())):
    answer = -1
    N = int(input())
    num_list = list(map(int, input().split()))
    for i in range(len(num_list)):
        if len(num_list) == 1:
            pass
        else:
            for j in range(i + 1, len(num_list)):
                temp = num_list[i] * num_list[j]
                if check(str(num_list[i] * num_list[j])):
                    answer = max(answer, temp)
    print("#{} {}".format(T + 1, answer))
