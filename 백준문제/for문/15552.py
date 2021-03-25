import sys
T = int(input()); result = []
for k in range(T):
    a, b = sys.stdin.readline().split()
    result.append(int(a)+int(b))
for k in range(T):
    print(result[k])
