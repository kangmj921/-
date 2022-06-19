def start_ladder(start):
    row, col = 0, start
    while row < 99:
        if col + 1 < 100 and ladder_list[row][col + 1]:
            while True:
                if col + 1 < 100 and ladder_list[row][col + 1]:
                    col += 1
                else:
                    break
            row += 1
        elif col - 1 >= 0 and ladder_list[row][col - 1]:
            while True:
                if col - 1 >= 0 and ladder_list[row][col - 1]:
                    col -= 1
                else:
                    break
            row += 1
        else:
            row += 1
    if ladder_list[row][col] == 2:
        return True
    else:
        return False


for _ in range(10):
    N = int(input())
    answer = 0
    cnt = 0
    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if ladder_list[0][i]:
            if start_ladder(i):
                answer = i
                break
    print("#{} {}".format(N, answer))
