import sys


#나이트를 4번 이상 이동 시킬 경우 모든 이동 방법을 써야함
#나이트를 3번 이하 이동 시킬 경우 한 가지 방법만 이용해도 됨
#나이트는 항상 오른쪽으로 이동할 수 밖에 없다.
#모든 반례에 대해 찾는게 힘든 문제..그리디를 생각하는 건 어렵지 않았다.
#https://it-college-diary.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1783%EB%B2%88-%EB%B3%91%EB%93%A0-%EB%82%98%EC%9D%B4%ED%8A%B8 설명 잘 되어있다.
N, M = map(int, sys.stdin.readline().split())
move_list = [[2, 1], [1, 2], [-1, 2], [-2, 1]]
result = 1
if N == 1 or M == 1:
    pass
elif N >= 3:
    if M >= 7:
        result += (M - 7) + 4
    elif M >= 4:
        result = 4
    else:
        result += (M - 1)
elif N == 2:
    if M >= 7:
        result += 3
    else:
        result = (M + 1) // 2
print(result)
