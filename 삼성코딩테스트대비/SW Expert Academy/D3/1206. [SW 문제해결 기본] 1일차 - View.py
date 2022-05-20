for T in range(10):
    apart_number = int(input())
    apart_length = list(map(int, input().split()))
    answer, temp = 0, 0
    for i in range(2, apart_number - 2):
        temp = apart_length[i] - max(apart_length[i - 1], apart_length[i - 2], apart_length[i + 1], apart_length[i + 2])
        if temp > 0:
            answer += temp
    print("#%d %d" % (T + 1, answer))
