for T in range(int(input())):
    N = int(input())
    answer = 0
    g_list = []
    for _ in range(N):
        g_list.append(int(input()))
    avg_g = sum(g_list) // N
    for i in g_list:
        if i < avg_g:
            answer += avg_g - i
    print("#{} {}".format(T + 1, answer))
