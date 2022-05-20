for T in range(10):
    N = int(input())
    table_list, answer = [], 0
    for _ in range(N):
        table_list.append(list(map(int, input().split())))
    for i in range(N):
        last_p = 0
        for j in range(N):
            if last_p != 1 and table_list[j][i] == 1:
                last_p = 1
            elif last_p == 1 and table_list[j][i] == 2:
                answer += 1
                last_p = 2
    print("#{} {}".format(T + 1, answer))
