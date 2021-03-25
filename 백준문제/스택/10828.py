import sys


if __name__ == '__main__':
    stack = list()
    for Test_Case in range(int(sys.stdin.readline())):
        command = sys.stdin.readline()
        if command == 'pop\n':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == 'size\n':
            print(len(stack))
        elif command == 'empty\n':
            if not stack:
                print(1)
            else:
                print(0)
        elif command == 'top\n':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        else:
            c, target_number = command.split()
            stack.append(int(target_number))