import sys

A, B, C = (map(int, sys.stdin.readline().split()))
num_of_prod = 0
if (C - B) <= 0:
    num_of_prod = -1
else:
    num_of_prod = A // (C - B) + 1
print(num_of_prod)
