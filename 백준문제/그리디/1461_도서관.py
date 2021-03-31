import sys

n, m = map(int, input().split())
book = list(map(int, sys.stdin.readline().split()))

# 음수, 양수 나누기
left = []
right = []
for i in book:
    if i < 0:
        left.append(i)
    elif i > 0:
        right.append(i)

distance = []
left.sort()
for i in range(len(left) // m):
    distance.append(abs(left[m * i]))
if len(left) % m > 0:
    distance.append(abs(left[(len(left) // m) * m]))

right.sort(reverse=True)
for i in range(len(right) // m):
    distance.append(right[m * i])
if len(right) % m > 0:
    distance.append(right[(len(right) // m) * m])

distance.sort()
result = distance.pop()
result += 2 * sum(distance)
print(result)
