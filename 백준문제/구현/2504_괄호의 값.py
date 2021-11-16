# 올바른 괄호열인지 판단하는 법은 여는 괄호를 모두 스택에 넣고, 닫힌 괄호가
# 나올때마다 스택 맨위의 값이랑 짝이 맞는지 확인을 하면 된다.
# 먼저 올바른 괄호열인지 확인을 하고 괄호열의 값을 구하도록한다.
# 괄호열의 값을 구하는 부분을 구현하는 과정이 고민이 많았다.
# 우선적으로는 닫히는 괄호가 나왔을때, ), ]에 따라 값을 초기화한 뒤, 스택에 넣는다.
# 스택의 값이 괄호가 아닌 숫자인 경우, 괄호안에 있는 괄호열값이므로, 스택의 맨 위가 괄호가 될 때까지 빼서
# 모두 더한 뒤, 닫힌 괄호에 따라 2나 3을 곱해준다. 그리고 괄호 값을 스택에서 빼고
# 괄호열 결과값을 다시 스택에 넣어준다. 과정을 계속 반복하면 숫자들만 스택에 남고 다 더한 값이 최종적으로
# 구하는 괄호열값이다.

def check_True(string):             # 괄호열이 옳은 괄호열인지 먼저 판단
    stk, val = [], True
    for i in string:
        if i in '()[]':
            if i in '([':
                stk.append(i)
            else:
                if len(stk) == 0:   # 닫힌 괄호가 짝이 없는 경우
                    return False
                if i == ')' and stk[-1] == '(':     # 닫힌 괄호의 짝이 맞는지 확인
                    stk.pop()
                    continue
                if i == ']' and stk[-1] == '[':
                    stk.pop()
                    continue
                return False
        else:
            return False
    if len(stk) != 0:   # 열린 괄호가 짝이 없는 경우
        return False
    return val


input_string, stack = input(), []
if check_True(input_string):
    val_list, result = [], 0
    for i in range(len(input_string)):
        if input_string[i] in '([':
            stack.append(input_string[i])
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(2)
                continue
            if stack[-1] == '[':
                stack.pop()
                stack.append(3)
                continue
            temp = 0
            while type(stack[-1]) != str:   # 스택의 맨 위 값이 괄호가 될 때까지 스택의 값을 빼서 temp에 더함.
                temp += stack[-1]           # 결국 구해지는 temp 값은 괄호 안의 괄호열값이다.
                stack.pop()
            if stack.pop() == '(':      # 괄호에 따라 곱해지는 괄호안의 괄호열 값, 그리고 그 값을 다시 스택에 넣는다.
                stack.append(temp * 2)
            else:
                stack.append(temp * 3)
    print(sum(stack))
else:
    print(0)
