num_list = [False, False] + [True] * (10 ** 6 - 1)
prime_list = []
for i in range(2, len(num_list)):
    if num_list[i]:
        prime_list.append(i)
        for j in range(2 * i, len(num_list), i):
            num_list[j] = False


for T in range(int(input())):
    D, A, B = map(int, input().split())
    answer = 0
    for i in prime_list:
        if A <= i <= B:
            str_i = str(i)
            if str(D) in str_i:
                answer += 1
    print("#{} {}".format(T + 1, answer))
