# ai의 값을 최소화 하기 위해서는 더해지는 제곱수를 구하고
# 해당 수가 제곱근으로 나타내었을 때, 정수가 아닌 경우 구해진
# 제곱수 보다 작은 정수의 제곱을 원래 값에서 빼면서 뺀 값이
# 다시 제곱근으로 나타내었을 때, 정수가 되는지, 정수가 된다면
# 해당 값을 불러오면서 bottom-up 방식으로 해볼 것이다.
# DP로 할 경우, pypy3으로 통과를 하는데, python3에선 시간초과
# 더 효율적인 코드가 있는지 확인해본 결과, python3로 통과한
# 사람들은 완탐으로 해결하였는데, 최대 N의 값인 50000의 제곱근이
# 223.6067로 최대 네 개의 수의 제곱을 더한 것으로, 네 개의 for문을
# 돌려 해결하였다.
N = int(input())
num_list = [100] * 50001
num_list[1] = 1
for i in range(2, N + 1):
    if int(i ** 0.5) ** 2 == i:
        num_list[i] = 1
    else:
        for j in range(int(i ** 0.5), 0, -1):
            num_list[i] = min(num_list[i], num_list[j * j] + num_list[i - (j ** 2)])
print(num_list[N])
