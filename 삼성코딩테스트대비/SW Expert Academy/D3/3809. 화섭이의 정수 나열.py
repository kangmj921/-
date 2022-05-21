for T in range(int(input())):
    N = int(input())
    n_list = ''
    while True:
        n_list += ''.join(input().split())
        if len(n_list) == N:
            break
    target = 0
    while True:
        if str(target) not in n_list:
            print("#{} {}".format(T + 1, target))
            break
        else:
            target += 1
