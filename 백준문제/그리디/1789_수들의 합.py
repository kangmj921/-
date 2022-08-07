# 서로 다른 자연수 N개가 최대가 되려면 최대한 작은 수들로 S를 구성해야한다.
#
S = int(input())
n = 1
while n * (n + 1) // 2 <= S:
    n += 1
print(n - 1)