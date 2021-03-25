import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = []
result = 0
for i in range(N):
    coin_list.append(int(input()))
while K > 0:
    if coin_list[-1] > K:
        coin_list.pop()
    else:
        result += (K // coin_list[-1])
        K -= (K // coin_list[-1]) * coin_list[-1]
        coin_list.pop()
print(result)
