# 조합을 itertools 이용해서 구현해보고 싶어서 써봤다. 문제에선, 총 인원수가 20명까지라
# 각 팀을 뽑는 최대 경우의 수는 20C10 = 184756이고, 또 10명 내에서 능력치 수치를 구하려면
# 2명씩 또 조합을 만들어야 되니, 10C2 = 45, 즉 최대 184756 * 45 만 큼이 걸린다.
# 인원이 많아지면 시간초과에 걸리기 쉽다.
# 이를 막으려면, 조합부분에서 백트래킹이 필요할것 같다.
#
from itertools import combinations
import math


# def combination_by_dfs(index, list):
#     if len(list) == r:
#         answer.append(list[:])
#         return
#     for i in range(index, n):
#         dfs(i + 1, list + [origin_list[i]])



def get_score(team):
    result = 0
    for i, j in list(combinations(team, 2)):
        result += parameter_list[i - 1][j - 1] + parameter_list[j - 1][i - 1]
    return result


N = int(input())
parameter_list = [list(map(int, input().split())) for _ in range(N)]
answer = math.inf
a = list(combinations([i for i in range(1, N + 1)], N//2))
for i in range(len(a) // 2):
    S_team, L_team = a[i], a[len(a) - 1 - i]
    S_score = get_score(S_team)
    L_score = get_score(L_team)
    answer = min(answer, abs(S_score - L_score))
print(answer)
