for TC in range(int(input())):
    N = int(input())
    n_list = list(map(int, input().split()))
    answer = 0
    for i in range(1, N - 1):
        if n_list[i - 1] < n_list[i] < n_list[i + 1] or n_list[i + 1] < n_list[i] < n_list[i - 1]:
            answer += 1
    print("#{} {}".format(TC + 1, answer))