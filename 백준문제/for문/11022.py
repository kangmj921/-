import sys
T = int(input()); result = []; A = []; B = []
for k in range(T):
    a, b = sys.stdin.readline().split()
    A.append(a); B.append(b)
    a = int(a); b = int(b)
    result.append(a+b)
for k in range(T):
    print("Case #%d: %d + %d = %d" % (k+1, int(A[k]), int(B[k]), int(result[k])))