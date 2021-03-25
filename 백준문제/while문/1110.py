N = int(input())
A = 0
B = 0
n = 0
T = N
if N < 10:
    A = 0
    B = N
    N = 10 * B + (A + B)
    n += 1
else:
    A = N // 10
    B = N % 10
    N = 10 * B + ((A + B) % 10)
    n += 1
while N != T:
    if N < 10:
        A = 0
        B = N
        N = 10*B + ((A + B) % 10)
        n += 1
    else:
        A = N // 10
        B = N % 10
        N = 10*B + ((A + B) % 10)
        n += 1
print(n)