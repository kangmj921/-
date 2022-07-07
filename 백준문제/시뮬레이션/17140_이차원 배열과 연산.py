import itertools


def RC_function():
    len_A = 0
    for i in range(len(A_list)):
        count_num = [[i, 0] for i in range(101)]
        temp = []
        for j in range(len(A_list[i])):
            count_num[A_list[i][j]][1] += 1
        for k in range(1, 101):
            if count_num[k][1]:
                temp.append(count_num[k])
        temp.sort(key=lambda x: [x[1], x[0]])
        temp_by_list = list(itertools.chain(*temp))
        if len(temp_by_list) > 100:
            temp_by_list = temp_by_list[:101]
        A_list[i] = temp_by_list
        len_A = max(len_A, len(A_list[i]))
    for i in range(len(A_list)):
        for j in range(len_A - len(A_list[i])):
            A_list[i].append(0)


r, c, k = map(int, input().split())
A_list = [list(map(int, input().split())) for _ in range(3)]
# 행과 열의 크기는 100을 넘어갈 수 없음.
time = 0
while time <= 100:
    try:
        if A_list[r - 1][c - 1] == k:
            break
    except:
        pass
    if len(A_list) >= len(A_list[0]):  # 행의 개수 >= 열의 개수인 R연산
        RC_function()
    else:
        A_list = list(map(list, zip(*A_list)))
        # 열에 대해서 정렬하는 C연산은 행 열을 바꿔 R연산과 동일한 함수에서 실행할 수 있도록한다.
        RC_function()
        A_list = list(map(list, zip(*A_list)))
    time += 1
    # print(A_list)
if time == 101:
    time = -1
print(time)
