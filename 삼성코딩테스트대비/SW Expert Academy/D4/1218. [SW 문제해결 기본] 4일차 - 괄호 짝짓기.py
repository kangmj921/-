dict_ = {']' : '[', ')' : '(', '>' : '<', '}' : '{'}
for TC in range(10):
    n = int(input())
    input_string = list(input().rstrip())
    stack = []
    for i in range(n):
        temp = input_string[i]
        if temp in '{[(<':
            stack.append(temp)
        else:
            if stack:
                check = stack.pop()
                if dict_[temp] != check:
                    answer = 0
                    break
            else:
                answer = 0
                break
        answer = 1
    print("#{} {}".format(TC + 1, answer))
