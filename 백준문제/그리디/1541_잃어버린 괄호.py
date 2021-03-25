import sys


#최솟값을 만드려면, - 수식 이후의 값을 모두 빼준다고 생각하면 된다.
#최솟값을 만들기 위한 방법은 쉽게 생각했으니 이를 구현하는데 어려움이 있었다.
#쉽게 구현하는 방법은 -를 기준으로 문자열을 나누는 것.
#split을 활용할 줄 알아야겠다.
S = sys.stdin.readline().rstrip('\n').split('-')
result = 0
for i in range(len(S)):
    s = list(map(int, S[i].split('+')))
    if i == 0:
        result += sum(s)
    else:
        result -= sum(s)
print(result)
