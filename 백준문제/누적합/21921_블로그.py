N, X = map(int, input().split())
N_list = list(map(int, input().split()))

S_list = [N_list[0]]
answer = 0
n_dict = dict()
for i in range(1, N):
    S_list.append(S_list[-1] + N_list[i])
i, j = 0, X - 1
while True:
    # print(i, j)
    if j == N:
        break
    result = S_list[j] - S_list[i] + N_list[i]
    if n_dict.get(result) is None:
        n_dict[result] = 1
    else:
        n_dict[result] += 1
    answer = max(answer, result)
    i += 1
    j += 1
if not answer:
    print("SAD")
else:
    print(answer)
    print(n_dict[answer])