# E, S, M에 대하여 재귀함수를 돌면서 한 값이 나머지 보다 적을 때
# 그 값에 해당하는 값을 더해가는 브루트포스 방식으로 답을 구한다.
# 재귀함수를 오랜만에 사용하다 보니, 종료 조건을 어떻게 설정하는지
# 잘 생각해서 해야겠다.
import sys


def solution(a, b, c):
    if a == b and a == c and b == c:
        return a
    else:
        if a <= b and a <= c:
            return solution(a + 15, b, c)
        if b <= a and b <= c:
            return solution(a, b + 28, c)
        if c <= a and c <= b:
            return solution(a, b, c + 19)


sys.setrecursionlimit(10000)
E, S, M = map(int, input().split())
print(solution(E, S, M))
