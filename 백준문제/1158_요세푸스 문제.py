N, K = map(int, input().split())
n_list = [i for i in range(1, N + 1)]
idx = 0
answer = []
for i in range(N):  # O(N)
    idx += K - 1
    if len(n_list) <= idx:
        idx %= len(n_list)
    answer.append(n_list.pop(idx))  # O(N)
# 최대 O(25,000,000)
print('<', end='')
for i in range(len(answer)):
    if i != len(answer) - 1:
        print(answer[i], end=', ')
    else:
        print(answer[i], end='')
print('>')
