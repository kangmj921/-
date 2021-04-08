import sys

N, M = map(int, sys.stdin.readline().split())
ball_list = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(len(ball_list)):
    for j in range(i+1, len(ball_list)):
        if ball_list[j] != ball_list[i]:
            result += 1
print(result)