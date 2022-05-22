for T in range(int(input())):
    N = int(input())
    income_list = list(map(int, input().split()))
    income_avg = sum(income_list)/N
    answer = 0
    for i in income_list:
        if i <= income_avg:
            answer += 1
    print("#{} {}".format(T + 1, answer))
