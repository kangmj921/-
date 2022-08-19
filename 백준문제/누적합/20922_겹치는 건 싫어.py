N, K = map(int, input().split())
N_list = list(map(int, input().split()))
i, j = 0, 0
n_dict = dict()
answer = 0
while True:
    if j == N:
        answer = max(answer, j - i)
        break
    if n_dict.get(N_list[j]) is None:
        n_dict[N_list[j]] = 1
    else:
        if n_dict[N_list[j]] == K:
            answer = max(answer, j - i)
            n_dict[N_list[i]] -= 1
            i += 1
            continue
        else:
            n_dict[N_list[j]] += 1
    j += 1
print(answer)
