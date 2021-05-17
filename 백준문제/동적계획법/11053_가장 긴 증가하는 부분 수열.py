from collections import deque

N = int(input())
num_list = list(map(int, input().split()))
result = deque()
for i in range(N, 0, -1):
    stack = []
    if i == 0:
        result.append([num_list[-1]])
    else:
        stack.append()
print(result)
