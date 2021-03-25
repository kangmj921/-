import sys

D = {'(': ')', '[': ']'}


def check_bracket(in_str):
    open_stack = list()
    for k in range(len(in_str)):
        if in_str[k] is '[' or in_str[k] is '(':
            open_stack.append(in_str[k])
        else:
            if open_stack:
                c = D[open_stack.pop()]
            else:
                print('no')
                return
            if in_str[k] != c:
                print('no')
                return
    if open_stack:
        print('no')
        return
    else:
        print('yes')
        return


def new_input(input):
    i = 0
    new_i = list()
    while input[i] != '.':
        if input[i] is '[' or input[i] is ']' or input[i] is '(' or input[i] is ')':
            new_i.append(input[i])
        i += 1
    return new_i


if __name__ == '__main__':
    while True:
        input_str = list(sys.stdin.readline().rstrip('\n'))
        if input_str == ['.']:
            exit()
        else:
            input_str = new_input(input_str)
            check_bracket(input_str)