import math

M, N = map(int, input().split())
prime_number = [True] * (N + 1) #Bool 자료형의 리스트로 하는게 더 빠름

def get_primes(n):
    max_length = math.ceil(math.sqrt(n))

    prime_number[1] = False
    for start_num in range(2, max_length):
        if prime_number[start_num]:
            for i in range(start_num * 2, n+1, start_num):
                prime_number[i] = False # 소수가 아닌 index에 해당하는 원소를 False로

get_primes(N)
for p in range(M,N+1):
    if prime_number[p]:
        print(p)