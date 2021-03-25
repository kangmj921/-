arr = list()
arr2 = list()
for k in range(10):
    N = int(input())
    N %= 42
    arr.append(N)
    if arr2.count(N) < 1:
        arr2.append(N)
print(len(arr2))
