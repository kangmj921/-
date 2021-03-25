import sys


N = int(input())
coordinate = list()
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))
coordinate = sorted(coordinate, key=lambda x: (x[0], x[1]))
for i in coordinate:
    print(i[0], i[1])
