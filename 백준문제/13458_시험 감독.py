# 총 감독관은 오직 1명, 부감독관은 몇명이 있든 상관이 없으므로,
# 필요한 최소 감독관 수를 구하려면, 모든 시험장에 총 감독관을 1번 넣은다음
# 남은 응사자 수에 대한 부감독관의 수를 구한다.

# 처음엔 총 감독관이 없어도 되는 줄 알았으나, 아니었다..
import sys


N = int(input())
A_list = list(map(int, sys.stdin.readline().split()))
answer = 10 ** 9
B, C = map(int, input().split())
result = 0
for i in range(len(A_list)):
    temp = A_list[i]
    temp -= B
    result += 1
    if temp > 0:
        result += (temp // C) + (1 if temp % C else 0)
print(result)
