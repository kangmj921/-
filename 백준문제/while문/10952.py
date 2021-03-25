import sys
a, b = sys.stdin.readline().split()
A = int(a)
B = int(b)
arr = []
while (A != 0) & (B != 0):
    arr.append(A + B)
    a, b = sys.stdin.readline().split()
    A = int(a)
    B = int(b)
for k in range(len(arr)):
    print(int(arr[k]))
