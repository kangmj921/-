# LIS 알고리즘을 활용하여 풀 수 있는 문제.
# 증가 부분 수열을 찾으면서 dp값에 증가 부분 수열 원소의 합을
# 저장한다.
N = int(input())
num_list = list(map(int, input().split()))
dp_list = [0] * N
for i in range(N):
    dp_list[i] = num_list[i]
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_list[i] = max(dp_list[i], num_list[i] + dp_list[j])
print(max(dp_list))
