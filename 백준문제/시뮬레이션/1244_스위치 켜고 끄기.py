N = int(input())
switch_condition = list(map(int, input().split()))
on, off = 1, 0
for i in range(int(input())):
    sex, given_num = map(int, input().split())
    if sex == 1:            # 남학생이 부여받은 스위치 번호의 배수대로 스위치 상태를 변경하도록 함.
        multiple = given_num
        while given_num <= len(switch_condition):
            switch_condition[given_num - 1] = int(not switch_condition[given_num - 1])
            given_num += multiple
    else:
        start, end = given_num - 1, given_num + 1
        while True:         # 매 반복마다 부여받은 스위치 번호를 중심으로 좌우가 대칭인 구간을 찾고, 대칭이면 구간의 스위치 상태를 바꾼다.
            if start < 1 or end > len(switch_condition):
                break
            else:
                if switch_condition[start - 1] == switch_condition[end - 1]:
                    switch_condition[start - 1], switch_condition[end - 1] = int(not switch_condition[start - 1]), int(not switch_condition[end - 1])
                else:
                    break
            start -= 1
            end += 1
        switch_condition[given_num - 1] = int(not switch_condition[given_num - 1]) # 모든 대칭 구간의 스위치를 바꾼 후, 중심이었던 스위치 상태를 바꿈
for i in range(len(switch_condition)):
    if (i + 1) % 20 == 0 or i == len(switch_condition) - 1:
        print(switch_condition[i])
    else:
        print(switch_condition[i], end=" ")
