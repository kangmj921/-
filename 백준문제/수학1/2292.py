N = int(input())
start = 1
find_point = 1
i = 1
while find_point < N:
    find_point = start + 6 * i
    i += 1
    start = find_point
print(i)
