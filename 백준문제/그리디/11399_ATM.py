import sys

N = int(input())
P_list = list(map(int, sys.stdin.readline().split()))
P_list.sort()
result = 0
for i in range(len(P_list)):
    result += sum(P_list[:i+1])
print(result)
