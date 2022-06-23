def make_postfix(s):
    stack = []
    result = ''
    for i in s:
        if i == '*':
            while stack and (stack[-1] == '*'):
                result += stack.pop()
            stack.append(i)
        elif i == '+':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        else:
            result += i
    while stack:
        result += stack.pop()
    return result


def calculate_postfix(s):
    stack = []
    post_fix = make_postfix(s)
    for i in post_fix:
        if i in '*+':
            if i == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
        else:
            stack.append(int(i))
    return stack.pop()


for TC in range(10):
    N = int(input())
    input_string = input().rstrip()
    answer = calculate_postfix(input_string)
    print("#{} {}".format(TC + 1, answer))
