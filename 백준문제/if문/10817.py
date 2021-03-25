a, b, c = input().split()
if(int(a)>=int(b)):
    if(int(b)>=int(c)):
        print(b)
    else:
        if(int(a)>=int(c)):
            print(c)
        else:
            print(a)
else:
    if(int(a)>=int(c)):
        print(a)
    else:
        if(int(b)>=int(c)):
            print(c)
        else:
            print(b)