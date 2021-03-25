import sys

D = {'(': ')'}


def check_bracket(in_str):
    open_stack = list()
    for k in range(len(in_str)):
        if in_str[k] is '[' or in_str[k] is '(' or in_str[k] is '{':
            open_stack.append(in_str[k])
        else:
            if open_stack:
                c = D[open_stack.pop()]
            else:
                print('NO')
                return
            if in_str[k] != c:
                print('NO')
                return
    if open_stack:
        print('NO')
        return
    else:
        print('YES')
        return


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        input_str = list(sys.stdin.readline().rstrip('\n'))
        check_bracket(input_str)