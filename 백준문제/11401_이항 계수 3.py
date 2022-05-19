def factorial(n):
    temp = 1
    for i in range(2, n + 1):
        temp *= i
        temp %= p
    return temp


def div(n, a):
    if a == 1:
        return n % p
    temp = div(n, a // 2)
    if a % 2:
        return temp ** 2 * n % p
    else:
        return temp ** 2 % p


N, R = map(int, input().split())
p = 1000000007
A, B, answer = 1, 1, 1
A = factorial(N)
B = factorial(R) * factorial(N - R)
B = div(B, p - 2)
answer = A * B % p
print(answer)