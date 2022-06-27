# 카약을 빌릴때, 출발하지 못하는 팀이 최소가 되려면, 카약이 손상된 팀들이 가능한한 여분의 카약을 빌려야한다.
# 카약을 빌릴 수 있는 조건은 바로 다음이나 전에 해당하는 팀만 빌릴 수 있고, 빌린 카약은 다시 다른 팀에게 빌려 줄 수 없다.
# 각 팀 별로 카약의 수를 1로 먼저 초기화한다.
# 손상된 팀의 카약의 수를 0으로 초기화 한다.
# 여분이 있는 팀의 카약의 수를 +1 씩 해준다.
# 모든 리스트를 돌면서, 0인 팀이 있다면, 빌릴 수 있는 팀이 있는지 확인한다.
# 있다면 빌려주는 팀의 카약의 수를 -1 하고 빌린 팀의 카약의 수를 + 1 한다.
# 최종적으로 카약의 수가 0인 팀의 수를 구한다.
import sys

N, S, R = map(int, sys.stdin.readline().split())
team_list = [1] * (N + 2)
for c in list(map(int, sys.stdin.readline().split())):
    team_list[c] = 0
for c in list(map(int, sys.stdin.readline().split())):
    team_list[c] += 1
for i in range(1, N + 1):
    if not team_list[i]:
        if team_list[i - 1] == 2:
            team_list[i - 1] -=1
            team_list[i] += 1
        elif team_list[i + 1] == 2:
            team_list[i + 1] -= 1
            team_list[i] += 1
print(team_list.count(0))
