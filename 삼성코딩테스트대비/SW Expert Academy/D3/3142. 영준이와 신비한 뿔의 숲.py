for T in range(int(input())):
    n, m = map(int, input().split())
    num_of_u, num_of_t = 0, 0
    for i in range(m, -1, -1):
        num_of_u, num_of_t = m - i, i
        if (m - i) + 2 * i == n:
            break
    print("#{} {} {}".format(T + 1, num_of_u, num_of_t))
