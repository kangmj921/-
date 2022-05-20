for T in range(int(input())):
    N = int(input())
    num_list = list(map(int, input().split()))
    dp_list = [0] * N
    for i in range(N):
        dp_list[i] = 1
        for j in range(i):
            if num_list[j] < num_list[i]:
                dp_list[i] = max(dp_list[i], dp_list[j] + 1)
    answer = max(dp_list)
    print("#{} {}".format(T + 1, answer))
