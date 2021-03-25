import math


def get_primes(n):
    max_length = math.ceil(math.sqrt(n))
    for k in range(2, max_length):
        if prime_number[k]:
            for i in range(k+k, n+1, k):
                prime_number[i] = False

N = 1
try:
    while N > 0:
        N = int(input())
        prime_number = [True] * (2 * N + 1)
        prime_number[0] = False
        prime_number[1] = False
        if N > 1:
            get_primes(2*N)
            print(prime_number[N+1:2*N].count(True))
        elif N == 1:
            print(prime_number[:].count(True))
except:
    exit()