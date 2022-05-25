for T in range(int(input())):
    N, M = map(int, input().split())
    n_list = list(input().split())
    m_list = list(input().split())
    answer = 0
    set_n_m = set(n_list + m_list)
    answer = N + M - len(set_n_m)
    print("#{} {}".format(T + 1, answer))
