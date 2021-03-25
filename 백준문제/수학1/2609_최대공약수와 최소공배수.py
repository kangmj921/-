import math


def lcm(A, B):
    gcd = math.gcd(N, M)
    num1 = A / gcd
    num2 = B / gcd
    print(int(gcd*num1*num2))


N, M = map(int, input().split())
print(math.gcd(N, M))
lcm(N, M)
