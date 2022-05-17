def exponentitaion(n, m):
    global answer
    if m > 0:
        answer *= n
        exponentitaion(n, m - 1)
    return answer


for _ in range(10):
    T = int(input())
    N, M = map(int, input().split())
    answer = 1
    print("#{} {}".format(T, exponentitaion(N, M)))
