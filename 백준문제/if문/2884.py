a, b = input().split()
if(int(b)>=45):
    print(a, int(b)-45)
else:
    if(int(a)==0):
        a = "24"
    print(int(a)-1, (60+int(b))-45)