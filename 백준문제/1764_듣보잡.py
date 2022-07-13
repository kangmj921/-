import sys


d_dict = {}
stack = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    d_dict[sys.stdin.readline().rstrip()] = 1
for b in [sys.stdin.readline().rstrip() for _ in range(M)]:
    if d_dict.get(b):
        stack.append(b)
print(len(stack))
stack.sort()
for i in stack:
    print(i)
