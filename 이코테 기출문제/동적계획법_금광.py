for _ in range(int(input())):
    n, m = map(int, input().split())
    mine_list = list(map(int, input().split()))
    result = [0] * (len(mine_list) + 1)
    for i in range(1, n + 1):
        result[i * m] = mine_list[i * m]
    print(result[n * m])