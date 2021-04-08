import sys


def solution(L, start, end, via):
    via += 1
    if end - start > start:
        solution(L, start * 2, end, via)
    elif 2 < end - start < start:
        solution(L, start - 1, end, via)
    elif end - start < 2:
        solution(L, start + 1, end, via)



    # while start != end and start >= 0:
    #     if L[start] == 0:
    #         via += 1
    #         if L[start + 1] == 0:
    #             solution(L, start + 1, end, via)
    #         elif L[start - 1] == 0:
    #             solution(L, start - 1, end, via)
    #         elif L[start * 2] == 0:
    #             solution(L, start * 2, end, via)
    #     else:
    #         start = end
    # return via


N, K = map(int, sys.stdin.readline().split())
n_list = [0 for i in range(K)]
print(solution(n_list, N, K, -1))
