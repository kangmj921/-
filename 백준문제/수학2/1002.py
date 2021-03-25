T = int(input())
for k in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    add = (r1 + r2) ** 2
    sub = (r1 - r2) ** 2
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if add < d:
            print(0)
        elif add == d:
            print(1)
        else:
            if sub == d:
                print(1)
            elif sub > d:
                print(0)
            else: print(2)
