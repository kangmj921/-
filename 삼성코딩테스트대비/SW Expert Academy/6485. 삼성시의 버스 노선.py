for T in range(int(input())):
    N = int(input())
    answer = []
    stop_list = {}
    for i in range(1, 5001):
        stop_list[i] = 0
    for _ in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            stop_list[i] += 1
    P = int(input())
    for i in range(P):
        answer.append(stop_list[int(input())])
    print("#{}".format(T + 1), *answer)
