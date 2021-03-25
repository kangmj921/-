import sys
C = int(input())
for k in range(C):
    arr = list(map(int, sys.stdin.readline().split()))
    avg = sum(arr[1:len(arr)]) / arr[0]
    result = 0
    stu_ratio = 0
    for t in range(1, len(arr)):
        if arr[t] > avg:
            result += 1
    stu_ratio = result / arr[0] * 100
    print("%.3f" % round(stu_ratio,4) + "%")