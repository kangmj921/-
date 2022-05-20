# 구현하는데 가지치기와 규칙찾기를 잘해야 실행시간을 줄일수있다
def find_value(x, y):
    diag_num = x + y - 1
    temp = x - num_list_y[diag_num - 1][0]
    return num_list_y[diag_num - 1][2] + temp


def find_coordinate(n):
    for i in range(len(num_list_y)):
        if n < num_list_y[i][2]:
            temp = n - num_list_y[i - 1][2]
            if temp > 0:
                return num_list_y[i - 1][0] + temp, num_list_y[i - 1][1] - temp
        if n == num_list_y[i][2]:
            return num_list_y[i][0], num_list_y[i][1]


for T in range(int(input())):
    p, q = map(int, input().split())
    num_list_x = [(1, 1, 1)]
    num_list_y = [(1, 1, 1)]
    answer = 0
    for i in range(2, 301):
        n_y = num_list_y[-1][2] + i - 1
        num_list_y.append((1, i, n_y))
    p_x, p_y = find_coordinate(p)
    q_x, q_y = find_coordinate(q)
    p_q = (p_x + q_x, p_y + q_y)
    answer = find_value(p_q[0], p_q[1])
    print("#{} {}".format(T + 1, answer))
