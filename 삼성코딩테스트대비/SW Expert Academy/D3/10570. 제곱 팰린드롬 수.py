import math


for TC in range(int(input())):
    A, B = map(int, input().split())
    answer = 0
    for i in range(A, B + 1):
        string = str(i)
        check = True
        for j in range(len(string) // 2):
            if string[j] != string[len(string) - 1 - j]:
                check = False
                break
        if check:
            sqrt_i = math.sqrt(i)
            temp = int(sqrt_i)
            check = True
            if temp == sqrt_i:
                string = str(temp)
                if len(string) == 1:
                    answer += 1
                else:
                    for j in range(len(string) // 2):
                        if string[j] != string[len(string) - 1 - j]:
                            check = False
                            break
                        answer += 1
    print("#{} {}".format(TC + 1, answer))
