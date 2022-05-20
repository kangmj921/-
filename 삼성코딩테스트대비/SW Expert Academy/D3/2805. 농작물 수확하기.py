for T in range(int(input())):
    N = int(input())
    farm_data = []
    answer, k = 0, N // 2
    for _ in range(N):
        farm_data.append(list(map(int, input().rstrip('\n'))))
    for i in range(N // 2):
        # print(i, farm_data[i][k - i : k + i + 1], farm_data[N - 1 - i][k - i : k + i + 1])
        answer += sum(farm_data[i][k - i: k + i + 1]) + sum(farm_data[N - 1 - i][k - i: k + i + 1])
    answer += sum(farm_data[k])
    print("#{} {}".format(T + 1, answer))
