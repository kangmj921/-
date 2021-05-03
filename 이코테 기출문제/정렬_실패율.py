def solution(N, stages):
    answer = []
    total_player_num = len(stages)
    for i in range(1, N + 1):
        not_cleared_num = stages.count(i)
        if total_player_num == 0:
            fail = 0
        else:
            fail = not_cleared_num / total_player_num
        answer.append((i, fail))
        total_player_num -= not_cleared_num
    answer.sort(reverse=True, key=lambda x : x[1])
    return [x[0] for x in answer]
