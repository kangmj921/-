T = int(input())
for c in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    for k in range(len(S)):
        for t in range(R):
            print(S[k],end="")
    print()
