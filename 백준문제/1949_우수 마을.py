# 마을이 최대 10000개 이므로, 조건을 모두 만족하기 위한 우수 마을의 수는
# 최대 5000개, 10000개 중 5000개를 뽑는 경우의 수는 엄청 많으므로,
# 완전탐색으로 할 수는 없다.

# 마을의 구조는 트리로 되어 있으므로, 1번 마을이 제일 위에 위치한 트리라 가정하고
# 1번 마을 부터 깊이 우선 탐색을 하기 위한 재귀로 진행하며 값을 구한다.
# 제일 위에 위치한 노드 부터 깊이 탐색하게 되면, 제일 밑에 위치한 노드와 인접한 노드 부터
# 선택했을 경우, 안 했을 경우의 최대 인구수가 저장되며, 한 단계씩 올라가며
# 값을 저장하게 된다.
# dp_list를 2개의 요소를 가지는 N개의 리스트로 구성하여, 각 마을을 선택했을 경우,
# 안했을 경우 구할 수 있는 최대 주민수를 저장한다.
# 1번 마을에서 시작해서 제일 깊이 들어가면, 5번 마을이다. 5번 마을은 인접한 마을이 없으므로
# dp_list에 변화가 없고, 그 위에 인접했던 4번 마을이 선택되는 경우, 선택되지 않는 경우
# dp_list 4번 마을에 값의 변화가 생긴다.
# 그리고 트리의 노드를 모두 깊이 우선 탐색하면서,
# 각 마을을 선택하지 않을 경우, 선택했을 경우 최대 인구수를 구하게 된다.
import sys
sys.setrecursionlimit(10 ** 9)


def search(start_node):
    visit[start_node] = 1
    for i in village_list[start_node]:  # i는 현재 깊이의 노드와 인접한 노드
        if not visit[i]:
            search(i)
            dp_list[start_node][1] += dp_list[i][0]
            # 현재 깊이의 노드가 선택되었으므로, 다음 깊이의 노드는 선택 불가능.
            # 현재 선택된 노드의 인구수
            dp_list[start_node][0] += max(dp_list[i][0], dp_list[i][1])
            # 현재 깊이의 노드가 선택되지 않았으므로 다음 깊이의 노드를 선택할 수 있거나 안함.
            # 두 가지 경우 중 최대값을 저장


N = int(input())
population = list(map(int, sys.stdin.readline().split()))
population.insert(0, 0)
village_list = [[] for _ in range(N + 1)]
dp_list = [[0, population[i]] for i in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    village_list[A].append(B)
    village_list[B].append(A)  # 마을은 트리 구조로 이루어져, 모두 연결되어 있으며
    # 길은 N - 1개임.
visit = [0] * (N + 1)
search(1)
print(max(dp_list[1][0], dp_list[1][1]))
