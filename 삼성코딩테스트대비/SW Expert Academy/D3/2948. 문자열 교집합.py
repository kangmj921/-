# set 자료형을 쓰면 간단해지는 문제이지만, set을 활용하지 못하는 조건이
# 주어진다면 set 자료형을 직접 구현해야(hast 알고리즘) 시간초과에 걸리지 않을것
# hash 알고리즘에 대해 알아야함.
for T in range(int(input())):
    N, M = map(int, input().split())
    n_list = list(input().split())
    m_list = list(input().split())
    answer = 0
    set_n_m = set(n_list + m_list)
    answer = N + M - len(set_n_m)
    print("#{} {}".format(T + 1, answer))
