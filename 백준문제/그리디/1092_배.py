import sys


# 시간초과 고민해보자...
#
def solution(b, c):
    result = 0
    count = 0
    start = len(b) - 1
    if b[-1] > c[-1]:
        return -1
    else:
        while count < M:
            for i in range(len(c) - 1, -1, -1):
                for j in range(start, -1, -1):
                    #print(b[j], start, c[i])
                    if c[i] >= b[j] != 0:
                        b[j] = 0
                        count += 1
                        start = j - 1
                        if b[j] == b[-1]:
                            b.pop()
                        break
            start = len(b) - 1
            result += 1
            #print(result, start, b)
    return result


N = int(input())
crane_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
box_list = list(map(int, sys.stdin.readline().split()))
crane_list.sort()
box_list.sort()
print(solution(box_list, crane_list))
