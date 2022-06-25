# 에라토스테네스의 체를 이용하여 범위에 주어진 모든 소수를 구한후,
# 문제에서 요구하는 M이상 N이하의 소수를 출력하면된다.
# 에라토스테네스의 체는 2부터 시작하여 배수를 모두 지우고
# 남은 수 중 제일 작은 수를 다시 선택해서 배수를 지우는 과정을
# 범위만큼 반복하는 과정이다.
M, N = map(int, input().split())
prime_number = [True] * (1000000 + 1)  # Bool 자료형의 리스트로 하는게 더 빠름


def get_primes():
    prime_number[1] = False
    for start_num in range(2, len(prime_number)):
        if prime_number[start_num]:
            for i in range(start_num * 2, len(prime_number), start_num):
                prime_number[i] = False  # 소수가 아닌 index에 해당하는 원소를 False로


get_primes()
for p in range(M, N+1):
    if prime_number[p]:
        print(p)
