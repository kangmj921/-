paint_count = list()


def re_paint(L):
    for a in range(len(L) - 7):
        for i in range(len(L[0]) - 7):
            num1 = 0
            num2 = 0
            for b in range(a, a + 8):
                for j in range(i, i + 8):
                    if (j + b) % 2 == 0:
                        if L[b][j] != 'W': num1 += 1
                        if L[b][j] != 'B': num2 += 1
                    else:
                        if L[b][j] != 'B': num1 += 1
                        if L[b][j] != 'W': num2 += 1
            paint_count.append(num1)
            paint_count.append(num2)


N, M = map(int, input().split())
chess = list()
#r = open("sample_input.txt", 'r')
for i in range(N):
    #chess.append(list(r.readline().strip('\n')))
    chess.append(input())
re_paint(chess)
print(min(paint_count))
