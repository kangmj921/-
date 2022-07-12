N = int(input())
n_list = [0] * 20000001
for i in list(map(int, input().split())):
    mid = 10000000
    if i < 0:
        idx = i * -1
        n_list[idx] = 1
    else:
        n_list[mid + i] = 1
M = int(input())
for j in list(map(int, input().split())):
    if j < 0:
        idx = j * -1
    else:
        idx = j + mid
    if n_list[idx]:
        print(1, end=" ")
    else:
        print(0, end=" ")
