# i부터 j번째 까지의 원소의 합은 곧
# j번째까지의 누적합 - i번째까지의 누적합 + i 번째 원소의 값으로 나타낼 수 있다.
import sys


N, M = map(int, input().split())
N_list = list(map(int, sys.stdin.readline().split()))
S = [N_list[0]]
for i in range(1, N):
    S.append(S[-1] + N_list[i])
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
        print(N_list[i - 1])
    else:
        result = S[j - 1]
        if i > 1:
            result -= S[i - 1]
            result += N_list[i - 1]
        print(result)
