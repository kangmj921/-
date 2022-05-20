for T in range(int(input())):
    N, K = map(int, input().split())
    student_list = [0] * (N + 1)
    submitted_list = list(map(int, input().split()))
    answer = ''
    for i in submitted_list:
        student_list[i] = 1
    for i in range(1, len(student_list)):
        if not student_list[i]:
            answer += str(i) + ' '
    print("#{} {}".format(T + 1, answer))
