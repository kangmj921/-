T = int(input()); str = "*"
N = T; blk = ""
for k in range(T):
    for t in range(N-1):
        blk = blk + " "
    print(blk + str)
    str = str + "*"
    N = N-1; blk = ""
