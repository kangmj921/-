S = list(input())
alphabet = ['a','b','c','d','e','f',
            'g','h','i','j','k','l',
            'm','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
for k in range(len(alphabet)):
    if alphabet[k] in S:
        print(S.index(alphabet[k]),end=" ")
    else:
        print("-1",end=" ")