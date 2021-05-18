# LIS 알고리즘을 이용해서 풀 수 있는 문제이다.
# 이 문제는 반대로 내림차순으로 만들 수 있는 가장 긴 부분 수열의 길이
# 를 요구한다.
N = int(input())
soldier_list = list(map(int, input().split()))
dp_list = [0] * N
for i in range(N):
    dp_list[i] = 1
    for j in range(i):
        if soldier_list[i] < soldier_list[j]:
            dp_list[i] = max(dp_list[i], 1 + dp_list[j])
print(N - max(dp_list))
