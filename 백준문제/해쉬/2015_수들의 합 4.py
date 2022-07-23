N, K = map(int, input().split())
A = list(map(int, input().split()))
# A[i] 부터 A[j] 까지의 합은 S[j] - S[i - 1]로 나타낼 수 있다.
S = 0
answer = 0
hash_table = {0: 1}
for i in range(N):
    S += A[i]
    if S - K in hash_table.keys():
        answer += hash_table[S - K]
    if S in hash_table.keys():
        hash_table[S] += 1
    else:
        hash_table[S] = 1
print(answer)
