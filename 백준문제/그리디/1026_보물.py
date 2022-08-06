# S를 구하는 공식은 S = A[0] × B[0] + ... + A[N-1] × B[N-1] 이다.
# S를 가장 작게 만들기 위해선, 가장 큰 B의 수와 가장 작은 A의 수를 곱하면 된다.
# A는 작은 순으로 정렬하고, B는 큰 순으로 정렬한 뒤, 같은 index에 위치한 값끼리 곱해서
# 최소의 S를 얻을 수 있다.
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)