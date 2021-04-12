# 비트마스킹 문제, 파이썬으로 비트 마스킹을 해볼 수 있는 문제였다.
def solution(c, t):
    max_seat = 20
    if c[0] in '12':
        command_num, train_index, seat_num = map(int, c.split())
    else:
        command_num, train_index = map(int, c.split())
    if command_num == 1:
        t[train_index] = t[train_index] | (2 ** (seat_num - 1))
    elif command_num == 2:
        if t[train_index] & (2 ** (seat_num - 1)):
            t[train_index] = t[train_index] ^ (2 ** (seat_num - 1))
    elif command_num == 3:
        if t[train_index] & (2 ** (max_seat - 1)):
            t[train_index] = t[train_index] ^ (2 ** (max_seat - 1))
        t[train_index] *= 2
    else:
        t[train_index] = int(t[train_index] / 2)


N, M = map(int, input().split())
train_list = [0] * (N + 1)

for i in range(M):
    command = input().rstrip('\n')
    solution(command, train_list)
train_list[0] = 1e9
print(len(set(train_list))-1)
