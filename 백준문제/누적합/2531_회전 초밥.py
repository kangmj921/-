from collections import deque
import sys


N, d, k, c = map(int, input().split())
chobab_list = []
for _ in range(N):
    chobab_list.append(int(sys.stdin.readline()))
result_list = chobab_list[:k]
answer = len(set(result_list + [c]))
for i in range(1, N):
    end = (i + k - 1) % N
    result_list = deque(result_list)
    result_list.popleft()
    result_list.append(chobab_list[end])
    temp = list(result_list) + [c]
    answer = max(answer, len(set(temp)))
print(answer)
