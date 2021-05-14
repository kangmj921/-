N, M = map(int, input().split())
coin_list = [0] * (M + 1)
for _ in range(N):
    coin_list[int(input())] = 1

