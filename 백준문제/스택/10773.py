import sys


if __name__ == '__main__':
    stack = list()
    for Test_case in range(int(sys.stdin.readline())):
        N = int(sys.stdin.readline())
        if N == 0:
            stack.pop()
        else:
            stack.append(N)
    print(sum(stack))
