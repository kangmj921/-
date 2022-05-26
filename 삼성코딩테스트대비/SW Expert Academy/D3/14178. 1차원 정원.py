for T in range(int(input())):
    N, D = map(int, input().split())
    answer = 1
    start = 1 + D  # 분무기가 제일 낮은 좌표(1)을 뿌리기 위한 현재 위치
    end = 1 + 2 * D  # 분무기가 제일 낮은 좌표를 뿌리는 위치일때, 제일 높이 뿌릴 수 있는 위치
    while True:
        if N > start:
            if N > end:
                answer += 1
                start = end + D + 1
                end = start + D
            else:
                break
        else:
            break
    print("#{} {}".format(T + 1, answer))
