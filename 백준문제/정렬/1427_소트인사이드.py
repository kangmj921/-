N = list(map(int, input().rstrip('\n')))
N.sort(reverse=True)
for i in N:
    print(i, end="")
