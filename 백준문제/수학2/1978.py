import sys
N = int(input())
S = sys.stdin.readline()
list_s = list(map(int, S.split()))
result = len(list_s)
for t in range(len(list_s)):
    for k in range(2, max(list_s) + 1):
        if list_s[t] % k == 0 and list_s[t] != k:
            result -= 1
            break
        else:
            result += 0
if 1 in list_s:
    print(result-1)
else:
    print(result)
