# 큰 수를 구하는 경우 자리 수를 계속 늘려 주면 되기에
# 최소의 성냥개비를 소비하는 2와 7로만 구성해서 최대한 자리수를 늘린다.
# 작은 수를 구하는 경우 한 자리수에 최대한 많은 성냥개비를 써야한다.
# 한 자리수마다 7개를 쓰는게 베스트지만, 남은 성냥개비 수를 고려해야한다.
# 남는 성냥개비의 수가 1이면 안되니까, 6개를 선택하고 2개를 남기는 식으로 해야한다.
# 위와 같은 식으로 예외처리를 계속 해주면 됨....
num_list = {2: '1', 3: '7', 4: '4', 5: '235', 6: '069', 7: '8'}
str_list = [2, 3, 4, 5, 6, 7]


def make_small(n):
    answer = ''
    if n <= 7:
        temp.append(n)
    else:
        for i in range(n // 7):
            temp.append(7)
        if n % 7 == 1:
            temp[-1] = 6
            temp.append(2)
        elif n % 7 == 2:
            temp.append(2)
        elif n % 7 == 3:
            if n == 10:
                temp[-1] = 5
            else:
                temp[-1], temp[-2] = 6, 6
            temp.append(5)
        elif n % 7 == 4:
            temp[-1] = 6
            temp.append(5)
        elif n % 7 == 5:
            temp.append(5)
        elif n % 7 == 6:
            temp.append(6)
    for i in range(len(temp) - 1, -1, -1):
        num = num_list[temp[i]]
        if len(num) == 1:
            answer += num[0]
        elif temp[i] == 6 and i == len(temp) - 1:
            answer += num[1]
        else:
            answer += num[0]
    return answer


def make_big(n):
    answer = ''
    if n % 2 == 0:
        for i in range(n // 2):
            answer += '1'
    else:
        answer = '7'
        for i in range(n // 2 - 1):
            answer += '1'
    return answer


for T in range(int(input())):
    n = int(input())
    temp = []
    print(int(make_small(n)), end=" ")
    print(int(make_big(n)))
