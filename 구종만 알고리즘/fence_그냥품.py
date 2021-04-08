import sys


def fence(h, start, end, sq):
    if len(h) == 0:
        sq.append(0)
        return
    result = h[start]; i = end
    #print(start, end)
    if len(h) == 1:
        sq.append(h[0])
        return
    if len(h) > end > start:
        if h[start] > h[end]:
            if h[start] < h[end] * 2:
                sq.append(h[end] * 2)
            else:
                sq.append(h[start] * (end - start))
                #print("sq", sq)
            fence(h, start + 1, end + 1, sq)
        else:
            while i < len(h) and h[start] <= h[i]:
                result += h[start]
                i += 1
            #print("result", result)
            k = start -1
            while k >= 0 and h[k] > h[start]:
                result += h[start]
                k -= 1
            if result < h[end]:
                sq.append(h[end])
            else:
                sq.append(result)
            #print("sq", sq)
            fence(h, start + 1, end + 1, sq)
    else:
        return


for C in range(int(input())):
    square = list()
    N = int(input())
    if N != 0:
        height = list(map(int, sys.stdin.readline().split()))
        #print(height, len(height))
        fence(height, 0, 1, square)
    #print(square)
        print(max(square))
    else:
        print(0)

