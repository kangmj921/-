import sys


# 두 가지 성적에 대해 한 성적에서 제일 높은 사람을 먼저 뽑고 그 사람보다 다른 성적이 더 좋은
# 사람을 뽑도록 하였다. 실행시간이 4100ms 정도인데, 1800ms 인 사람의 코드를 살펴보니 sorted
# 함수를 사용하지 않고 첫번째 성적을 index로 두번째 성적을 해당 index의 값으로 받아서 index 1의
# 값을 이용하여 최종적으로 값을 구하였다. 첫번째 성적의 값이 전체 사원중의 순위인 값이라 index를 활용할
# 수 있었기 때문인것같다.
def solution(A):
    result_list1 = [A[0]]
    for x, y in A:
        a, b = result_list1[-1]
        if x <= a or y <= b:
            result_list1.append((x, y))
    # print(result_list1, result_list2)
    return len(result_list1) - 1


T = int(input())
for i in range(T):
    N = int(sys.stdin.readline())
    member_list = []
    for i in range(N):
        member_list.append(tuple(map(int, sys.stdin.readline().split())))
    a = sorted(member_list, key=lambda x:x[0])
    print(solution(a))
