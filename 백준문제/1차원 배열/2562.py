arr = list()
k = 0
while True:
    try:
        N = int(input())
        arr.insert(k, N)
        k += 1
    except:
        break
print(max(arr))
print(arr.index(max(arr))+1)
