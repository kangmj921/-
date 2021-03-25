import sys


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    stack = [i+1 for i in range(N)]
    print("<", end="")
    next_index = K - 1
    for k in range(1, N):
        if next_index >= len(stack):
            next_index = next_index % len(stack)
        print(stack.pop(next_index), end="")
        next_index += (K - 1)
        print(', ', end='')
    print('{0}'.format(stack[0])+'>')
