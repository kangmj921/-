import sys


#모든 수를 1로 바꿀 경우, 모든 수를 0으로 바꿀 경우 중 둘 중 최소로 수를 바꾸는것을 출력
S = list(map(int, sys.stdin.readline().rstrip('\n')))
count0 = 0
count1 = 0
i = 0
if S[0] == 1:
    count0 += 1
else:
    count1 += 1
for i in range(len(S)-1):
    if S[i] != S[i + 1]:
        if S[i + 1] == 1:
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
