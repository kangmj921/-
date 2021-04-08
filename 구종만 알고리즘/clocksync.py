switch_type = [[0, 1, 2],
               [3, 7, 9, 11],
               [4, 10, 14, 15],
               [0, 4, 5, 6, 7],
               [6, 7, 8, 10, 12],
               [0, 2, 14, 15],
               [3, 14, 15],
               [4, 5, 7, 14, 15],
               [1, 2, 3, 4, 5],
               [3, 4, 5, 9, 13]]
switch_num_order = [4, 1, 4, 9]
switch_clock_order = [8, 11, 12, 13]
switch_input_num = 0
INF = 9999


def judge_12(clock):
    if clock.count(0) == 16:
        return True
    else:
        return False


def input_switch(switch_num, clock):
    for j in range(len(switch_type[switch_num])):
        if clock[switch_type[switch_num][j]] > 0:
            clock[switch_type[switch_num][j]] -= 1
        else:
            clock[switch_type[switch_num][j]] += 3


def judge_unique_num(clock):
    ret = 0
    for i in range(len(switch_num_order)):
        if clock[switch_clock_order[i]] != 0:
            for j in range(clock[switch_clock_order[i]]):
                ret += clock[switch_clock_order[i]]
                input_switch(switch_num_order[i], clock)
    return ret


def sync_clock(clock, n):
    if n == len(switch_type):
        if judge_12(clock):
            return 0
        else:
            return INF
    if n in switch_num_order:
        sync_clock(clock, n + 1)
    ret = INF
    for cnt in range(4):
        ret = min(ret, cnt + sync_clock(clock, n + 1))
        input_switch(n, clock)
    return ret


for c in range(int(input())):
    clock_type = list(map(lambda x: (12 - int(x)) // 3, input().split()))
    if clock_type[14] != clock_type[15] or clock_type[8] != clock_type[12]:
        print(-1)
    else:
        print(judge_unique_num(clock_type) + sync_clock(clock_type, 0))
