N = int(input())
switch_condition = list(map(int, input().split()))
on, off = 1, 0
for i in range(int(input())):
    sex, given_num = map(int, input().split())
    if sex == 1:
        multiple = given_num
        while given_num <= len(switch_condition):
            switch_condition[given_num - 1] = int(not switch_condition[given_num - 1])
            given_num += multiple
    else:
        start, end = given_num - 1, given_num + 1
        while True:
            if start < 1 or end > len(switch_condition):
                break
            else:
                if switch_condition[start - 1] == switch_condition[end - 1]:
                    switch_condition[start - 1], switch_condition[end - 1] = int(not switch_condition[start - 1]), int(not switch_condition[end - 1])
                else:
                    break
            start -= 1
            end += 1
        switch_condition[given_num - 1] = int(not switch_condition[given_num - 1])
for i in range(len(switch_condition)):
    if (i + 1) % 20 == 0 or i == len(switch_condition) - 1:
        print(switch_condition[i])
    else:
        print(switch_condition[i], end=" ")
