# dp로 factorial 계산 과정을 구현해서 풀 수 있는 간단한 문제였다.
# 하지만 계산 결과를 출력할때, 실수 값을 int형 자료형으로 변환하여
# 구하게 되면 답을 얻을 수 없고, 대신 //을 사용하였을때는 답을 얻을
# 수 있었는데, 그 이유로는 실수를 부동 소수점 방식으로 표현하는 방식
# 에서 오차가 발생한다는 점이다.
# 따라서 실수 간에 계산을 하는 과정에서 오차가 생기게 되고,
# 이를 뒤늦게 int형 자료형으로 변환시켜도 오차가 생겼던 상태에서
# 변환이 되므로 최종적인 결과에 오차가 생기게 된다.
def factorial_by_dp(num):
    dp_list = [0] * (num + 1)
    if num == 0:
        return 1
    dp_list[1] = 1
    for i in range(2, num + 1):
        dp_list[i] = i * dp_list[i - 1]
    return dp_list[num]


n, m = map(int, input().split())
print(factorial_by_dp(n)//(factorial_by_dp(n - m) * factorial_by_dp(m)))
