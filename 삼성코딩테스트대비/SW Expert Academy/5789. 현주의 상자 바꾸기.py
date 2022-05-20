for T in range(int(input())):
    answer = ''
    N, Q = map(int, input().split())
    box_list = [0] * (N + 1)
    for i in range(1, Q + 1):
        l, r = map(int, input().split())
        box_list[l:r + 1] = [i] * (r - l + 1)
    for i in range(1, N + 1):
        answer += str(box_list[i]) + " "
    print("#{} {}".format(T + 1, answer))
