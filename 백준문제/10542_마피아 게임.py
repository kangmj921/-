# 마피아는 무조건 시민을 지목할 것이고, 시민은 마피아를 지목할 수도, 시민을 지목할 수도 있다.
# 아예 지목되지 않은 사람은 시민일 수도 마피아일 수도 있지만, 문제에선 최대 마피아의 수를
# 구하는 것이므로, 무조건 마피아라고 가정한다.
# 리스트의 i번째 원소는 i번 참가자를 지목한 참가자 목록이다.

# 먼저 각 노드를 확인해서 아무에게도 지목 안된 노드를 마피아라고 확정하고, 그 마피아가 지목한 사람도
# 시민으로 확정한다. 마피아나 시민으로 확정된 노드는 제거한다.
# 그렇게 확정된 노드들을 제외하고 남겨진 노드들을 dfs 같은 탐색으로 탐색할때, 첫 번째로 탐색한 노드가
# 연결하는 간선이 있는 그래프 형식이라면 그래프 안에 시민 1명은 확정적이므로, 시민으로 치고,
# 노드를 제거한다. 그리고 아무에게도 지목 안된 노드를 마피아로 확정, 그 마피아가
# 지목한 노드도 시민으로 확정하고 확정된 노드 삭제 ... 노드가 모두 없어질때까지 반복....
# 노드의 삭제는 연결된 간선을 지움으로서 구현한다.

# 위 방법으로 찾지 못하는 반례가 있는 것 같길래 다른 방법으로 구현해보기로 하였다.
# 간단하게 dfs를 이용해서 모든 방법을 찾는 식으로 하고, 중간 중간에 백트래킹을 넣는 방식으로
# 구현방식을 바꾸었다. 앞서 했던 방식은 복잡해서 반례도 찾기 어려웠던것 같다.
import sys
sys.setrecursionlimit(10 ** 9)


def dfs(n, cnt):  # 실패한 구현,
    global answer
    next_node = graph_1[n][0]
    # print(n, pointed[n], pointed[next_node], answer)
    if cnt == 1 and pointed[n]:  # 첫 번째로 만나는 지목되는 간선이 있는 노드는 시민이라고
        # 확정시키고 노드를 지운다.
        visit[n] = [1, 0]
        pointed[n] = 0
        if pointed[next_node]:
            pointed[next_node] -= 1
        if not visit[next_node][0]:
            dfs(next_node, cnt + 1)
    else:  # 첫번째로 만나지 않았거나 지목된 노드가 아님.
        if not pointed[n]:  # 현재 노드를 지목한 사람이 없음 그러면 마피아임.
            visit[n] = [1, 1]
            answer += 1
            if not visit[next_node][0]:  # 마피아 다음 시민은 확정적임.
                pointed[next_node] = 0
                visit[next_node] = [1, 0]
                t = graph_1[next_node][0]  # 시민이 가르키는 노드
                if pointed[t]:
                    pointed[t] -= 1  # 시민도 지워질 예정이므로, 시민이 가리키던 간선 삭제
                if not visit[t][0]:  # 시민이 고른 노드로 탐색하러감.
                    dfs(t, cnt + 1)


def dfs_search(idx):
    if visit[idx]:
        return
    visit[idx] = 1
    if not graph_2[idx]:  # 해당 참가자를 지목한 참가자가 없을 경우, 이 참가자는 마피아임.
        mafia[idx] = 1
        return
    for check_mafia in graph_2[idx]:  # 해당 참가자를 지목한 참가자 중에 마피아가 있다면 이 참가자는 시민임.
        dfs_search(check_mafia)  # 깊이 우선 탐색으로 리프 노드 우선적으로 탐색함.
        if mafia[check_mafia] == 1:  # 리프 노드부터 탐색한 이후, 깊이 점점 올라오면서 확인됨.
            mafia[idx] = 0
    pointed_num = graph_1[idx]  # 해당 참가자가 지목한 참가자
    if mafia[pointed_num] == 1:  # 해당 참가자가 지목한 사람이 마피아면 이 참가자는 시민임.
        mafia[idx] = 0
    if mafia[idx] == -1:  # 아직 아무것도 정해지지 않은 참가자의 경우
        mafia[idx] = 1  # 해당 참가자를 마피아로 일단 넣고
        mafia[graph_1[idx]] = 0  # 해당 참가자가 지목한 사람을 시민으로 하고,
        for check_mafia in graph_2[idx]:  # 해당 참가자를 지목한 사람은 모두 시민이다.
            mafia[check_mafia] = 0
    dfs_search(pointed_num)  # 현재 참가자가 지목한 다음 사람을 확인함.


N = int(input())
answer = 0
graph_1 = [0] * (N + 1)
graph_2 = [[] for _ in range(N + 1)]
# visit = [[0, 0] for _ in range(N + 1)]
visit = [False] * (N + 1)
mafia = [-1] * (N + 1)
for i in range(1, N + 1):
    graph_1[i] = int(sys.stdin.readline())  # i번 참가자가 지목한 참가자를 나타냄.
    graph_2[graph_1[i]].append(i)  # i번 참가자를 지목한 참가자를 나타냄.
# stack1 = []
# for i in range(1, N + 1):
#     if not graph_2[i]:  # i번 참가자를 지목한 사람이 없음.
#         answer += 1
#         visit[i] = [1, 1]  # 지목 안된 노드 = 마피아 확정이므로 탐색에서 제외시키기 위해 미리 방문 표시
#         visit[graph_1[i][0]] = [1, 0]  # 지목 안된 노드에게 지목된 노드 = 시민 확정이므로 위와 같이 미리
#         # 마피아가 지목한 사람 = graph_1[i][0]
#         # 시민이 지목한 사람 = graph_1[graph_1[i][0]][0]
#         pointed[graph_1[i][0]] = 0
#         stack1.append(graph_1[graph_1[i][0]][0])
# stack1 = set(stack1)
# for i in stack1:  # 시민으로 확정된 노드를 무시할거기 때문에 시민으로 확정된 노드가 연결한 간선 삭제
#     if pointed[i]:
#         pointed[i] -= 1
for i in range(1, N + 1):
    dfs_search(i)
print(mafia.count(1))
