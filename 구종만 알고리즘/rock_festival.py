import sys
C = int(sys.stdin.readline())
min_avg = list()
for k in range(C):
    N, L = map(int, input().split())
    arr_L = list(map(int, input().split()))
    av = list()
    for p in range(N - L + 1):
        n1 = p
        total = 0
        avg = 0
        total = sum(arr_L[p:p+L])
        n2 = p+L
        for t in range(N-n2+1):
            avg = total / (n2-p)
            av.append(avg)
            if n2 < N:
                total += arr_L[n2]
                n2 += 1
            else:
                break
    print("%.12f" % min(av))