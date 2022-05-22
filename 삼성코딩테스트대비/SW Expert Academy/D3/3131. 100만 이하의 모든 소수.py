# 에라토스테네스의 체 이용하는 문제
N = [False, False] + [True] * (10 ** 6)
prime_list = []
for i in range(2, 10**6):
    if N[i]:
        prime_list.append(i)
        for j in range(2 * i, 10**6 + 1, i):
            N[j] = False
print(*prime_list)
