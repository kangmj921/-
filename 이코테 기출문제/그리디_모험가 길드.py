import sys


# 뒤에서부터 공포도를 하나씩 확인해서 앞의 모험가의 수가 공포도 보다 같거나 많으면 그룹으로 설정
# def solution(s_list):
#     s_list.sort()
#     result = 0
#     while s_list[-1] > N:
#         s_list.pop()
#         if len(s_list) == 0:
#             return result
#     temp = len(s_list)
#     a = s_list.pop()
#     if a == 1:
#         result += 1
#     while len(s_list) > 0:
#         if temp - a >= 0:
#             temp -= a
#             result += 1
#         a = s_list.pop()
#     return result


#앞에서부터 공포도를 하나씩 확인하며 현재 그룹에 포함된 모험가의 수가 현재 확인하는 공포도 보다 크거나 같으면 그룹으로 설정.
def solution(s_list):
    count = 0
    result = 0
    for i in s_list:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result


N = int(input())
stat_list = list(map(int, sys.stdin.readline().split()))
print(solution(stat_list))