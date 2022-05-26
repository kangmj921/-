for TC in range(int(input())):
    N = int(input())
    line_list = [[] for _ in range(N)]
    answer = 0
    for i in range(N):
        line_list[i] = list(map(int, input().split()))
    for i in range(N - 1):
        for j in range(i + 1, N):
            start1, end1 = line_list[i]
            start2, end2 = line_list[j]
            if (start1 > start2 and end1 < end2) or (start1 < start2 and end1 > end2):
                answer += 1
    print("#{} {}".format(TC + 1, answer))
