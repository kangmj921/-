# a ^ p mod p = a mod p (a는 정수, p는 소수)
# a ^ (p - 1) mod p = 1 mod p
# a ^ (p - 2) mod p = 1/a mod p
# 역수는 특정값에 대해 곱셈으로 1이 되게 하는 수
# a의 역수는 a ^ (p - 2)
# nCr % p = (n!/(r!(n-r)!)) % p
# (n! * (r!(n-r)!) ^ -1) % p
# ((n! % p) * (r!(n-r)! ^ -1 % p)) % p
# (n! * (r!(n-r)! ^ (p - 2)) % p
def div(n, a):  # 거듭제곱은 분할 정복을 통해서 구현한다.
    if a == 1:
        return n % p
    temp = div(n, a // 2)
    if a % 2:
        return temp ** 2 * n % p
    else:
        return temp ** 2 % p


def factorial(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
        temp %= p
    return temp


for T in range(int(input())):
    N, R = map(int, input().split())
    p = 1234567891
    A, B, answer = 1, 1, 1
    A = factorial(N)
    B = factorial(R) * factorial(N - R)
    B = div(B, p - 2)
    answer = (A * B) % p
    print("#{} {}".format(T + 1, answer))
