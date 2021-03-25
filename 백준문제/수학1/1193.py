N = int(input())
d = 1
start = 0
end = 0
while end < N:
    end = start + d
    d += 1
    start = end
if (d-1) % 2 == 0:
    print("%d/%d" % ((d - 1) - start + N, 1 + start - N))
else:
    print("%d/%d" % (1 + start - N, (d - 1) - start + N))