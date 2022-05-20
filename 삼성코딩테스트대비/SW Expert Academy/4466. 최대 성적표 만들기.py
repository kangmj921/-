for T in range(int(input())):
    answer = 0
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    for i in range(K):
        answer += score_list[i]
    print("#{} {}".format(T + 1, answer))
