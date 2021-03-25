import sys


# def solution(index_number, start):
#     if index_number.count(1) == 3:
#         result = 0
#         for i in range(len(index_number)):
#             if index_number[i] == 1:
#                 result += num_list[i]
#         if result <= M and M - result <= M - result_list[-1]:
#             result_list[0] = result
#     else:
#         i = start
#         while i < len(index_number):
#             if index_number[i] == 0:
#                 index_number[i] = 1
#                 solution(index_number, i + 1)
#             index_number[i] = 0
#             i += 1

def solution(maximum):
    temp = 0
    temp2 = 0
    result_list = []
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            for k in range(j+1, len(num_list)):
                temp = num_list[i] + num_list[j] + num_list[k]
                if temp2 < temp <= maximum:
                    if maximum - temp <= maximum - temp2:
                        result_list.append(temp)
                    temp2 = temp
    return result_list


N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
print(max(solution(M)))
