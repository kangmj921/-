# 간격을 1부터 최대가 되게 하는 x까지 하면서
# 각 간격에 대해 이진탐색을 이용하여 C개가 될 때 까지
# 공유기를 설치한다.
import sys


N, C = map(int, input().split())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline().rstrip('\n')))
num_list.sort()
start = 1
end = num_list[-1] - num_list[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    value = num_list[0]
    count = 1
    for i in range(1, N):
        if num_list[i] >= value + mid:
            value = num_list[i]
            count += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
