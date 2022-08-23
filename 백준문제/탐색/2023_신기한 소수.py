# 왼쪽 자리수 부터 소수인지 아닌지 판단하고
# 맞다면 다음 자리수 까지 포함한 숫자를 소수를 판단
# 이 과정을 N 깊이의 재귀로 구현한다.
# 소수인지 판단하는 것은 1개의 수를 소수인지 아닌지 판단하는 알고리즘 중
# 제곱근을 이용하는게 제일 빠르기에 그걸 이용하기로 하였다.
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def dfs(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if check_prime(temp):
                dfs(temp)


prime_list = [2, 3, 5, 7]
N = int(input())
for p in prime_list:
    dfs(p)
