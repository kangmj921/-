N = int(input())
switch_condition = list(map(int, input().split()))
on, off = 1, 0
for i in range(int(input())):
    sex, given_num = map(int, input().split())
    if sex == 1:
        temp = given_num
        while given_num <= len(switch_condition):
            print(given_num)
            switch_condition[given_num - 1] = int(not switch_condition[given_num - 1])
            given_num += temp
    else:
        start, end = given_num - 1, given_num + 1
        while True:
            if start < 1 or end > len(switch_condition):
                break
            else:
                if switch_condition[start - 1] == switch_condition[end - 1]:
                    switch_condition[start - 1], switch_condition[end - 1] = int(not switch_condition[start - 1]), int(not switch_condition[end - 1])
            start -= 1
            end += 1
        switch_condition[given_num - 1] = int(not switch_condition[given_num - 1])
    print(switch_condition)
for i in range(len(switch_condition)):
    if i % 20 == 0:
        print()
    print(switch_condition[i], end=" ")

