# math 라이브러리를 사용하면 시간제한에 안걸리게 됨.
# 일일히 비교보다 math 라이브러리의 실행속도가 더 빠른거같다.
import math
answer = []
for TC in range(int(input())):
    N = int(input())
    score = 0
    for _ in range(N):
        x, y = map(int, input().split())
        num = math.ceil(math.sqrt(x * x + y * y) / 20)
        if num <= 0:
            score += 10
        elif num <= 11:
            score += 11 - num
    answer.append("#{} {}".format(TC + 1, score))
for i in answer:
    print(i)
