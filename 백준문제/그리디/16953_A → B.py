import sys

A, B = map(int, sys.stdin.readline().split())
result = 1
while A != B:
    if B < A:
        result = -1
        break
    if B % 10 == 1:
        B -= 1
        B /= 10
    elif B % 2 == 0:
        B /= 2
    else:
        result = -1
        break
    result += 1
print(result)
