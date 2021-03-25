T = int(input()); result = []
for k in range(T):
    A, B = input().split()
    A = int(A); B = int(B)
    result.append(A+B)
for k in range(T):
    print(result[k])