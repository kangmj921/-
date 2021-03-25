import sys

N = int(input())
Deque = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        Deque.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        Deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(Deque) > 0:
            print(Deque.pop(0))
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(Deque) > 0:
            print(Deque.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Deque))
    elif command[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    else:
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])