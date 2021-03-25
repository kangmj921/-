import sys


def tile_(N):
    stack = [1, 2]
    index = 2
    while index < N:
        stack_last = stack.pop(0)
        stack.append((stack_last + stack[-1]) % 15746)
        index += 1
    return stack[-1]


if __name__=='__main__':
    input_num = int(sys.stdin.readline())
    stack = list()
    print(tile_(input_num))
