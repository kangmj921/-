result = 1


def factorial(n, result):
    if n > 0:
        result *= n
        factorial(n-1,result)
    else:
        print(result)


N = int(input())
factorial(N, result)
