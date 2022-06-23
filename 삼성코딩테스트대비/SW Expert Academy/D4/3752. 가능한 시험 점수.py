from collections import deque


for T in range(int(input())):
    N = int(input())
    answer = 0
    n_list = list(map(int, input().split()))
    score_list = [0] * (sum(n_list) + 1)
    queue = deque()
    queue.append((0, 0))
    score_list[0] = 1
    while queue:
        idx, cnt = queue.popleft()
        if idx == N:
            break
        n_cnt = cnt + n_list[idx]
        if not score_list[n_cnt]:
            score_list[n_cnt] = 1
            queue.append((idx + 1, n_cnt))
        queue.append((idx + 1, cnt))
    answer = score_list.count(1)
    print("#{} {}".format(T + 1, answer))
