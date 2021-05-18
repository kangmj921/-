# dp를 이용해서 풀 수 있는 핵심적인 유형 중 하나이다.
# LIS 알고리즘이라고 따로 이름이 붙어있기도 하다.
# 주어진 리스트에서 인덱스를 한 칸씩 늘려가면서
# 내부 반복문으로 인덱스보다 작은 인덱스들을 살펴보면서 값이 인덱스의
# 원소 값보다 작은 것이 있을 경우, 길이를 저장하는 리스트를 업데이트함.
# 이 때 시간복잡도는 O(N^2)이지만, N의 값이 최대 1,000이라
# 시간 제한에는 걸리지 않는다. N이 커지면 효율적으로 할 수 있도록
# 하는 방법을 생각해봐야겠다.
N = int(input())
num_list = list(map(int, input().split()))
length_list = [0] * N
for i in range(N):
    length_list[i] = 1
    for j in range(i):
        if num_list[j] < num_list[i]:
            length_list[i] = max(length_list[i], 1 + length_list[j])
print(max(length_list))
