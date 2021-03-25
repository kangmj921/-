import sys
n, x = sys.stdin.readline().split()
N = int(n); X = int(x)
arr = list(sys.stdin.readline().split())
for k in range(len(arr)):
    if(int(arr[k]) < X):
        print(int(arr[k]),end=" ") # print에 맨 뒤에 붙일 문자를 end로 정해줌
