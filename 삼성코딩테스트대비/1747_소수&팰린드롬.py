import sys


def find_prime(N):
    if N == 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return N


def pelindrom(M):
    a = str(M)
    b = a[::-1]
    if a != b:
        return False
    return M


N = int(sys.stdin.readline())
check = 1
num_list = []
while check != 0:
    if pelindrom(N) and find_prime(N):
        print(N)
        break
    else:
        N += 1
