import sys
N = int(input())
arr = list(sys.stdin.readline().split())
arr = list(map(int,arr))
print(min(arr),max(arr))