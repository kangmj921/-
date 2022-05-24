import math


for TC in range(int(input())):
    n = int(input())
    day_list = list(map(int, input().split()))
    answer = math.inf
    for i in range(len(day_list)):
        if day_list[i]:
            index = i
            temp_n = n
            temp_result = 0
            while temp_n:
                if day_list[index]:
                    temp_n -= 1
                temp_result += 1
                index = (index + 1) % 7
            answer = min(answer, temp_result)
    print("#{} {}".format(TC + 1, answer))
