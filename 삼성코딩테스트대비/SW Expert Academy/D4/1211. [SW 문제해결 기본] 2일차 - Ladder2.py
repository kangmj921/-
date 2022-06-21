def start_ladder(start):
    row, col, cnt = 0, start, 0
    while row < 99:
        if col + 1 < 100 and ladder_list[row][col + 1]:
            while True:
                if col + 1 < 100 and ladder_list[row][col + 1]:
                    col += 1
                    cnt += 1
                else:
                    break
            row += 1
        elif col - 1 >= 0 and ladder_list[row][col - 1]:
            while True:
                if col - 1 >= 0 and ladder_list[row][col - 1]:
                    col -= 1
                    cnt += 1
                else:
                    break
            row += 1
        else:
            row += 1
        cnt += 1
    return cnt


for _ in range(10):
    N = int(input())
    answer = 0
    result = 10 ** 9
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder_list[0][i]:
            temp = start_ladder(i)
            if temp < result:
                result = temp
                answer = i
    print("#{} {}".format(N, answer))
