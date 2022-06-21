# ? 때문에 모든 상태를 고려한 방문 배열을 짠 것은 좋았는데, 2 케이스를 통과하지 못하였다.
# 통과하지 못한 케이스는 ?에서 깊이 우선 탐색이 제대로 탐색하지 못하고 루프를 돌거나 목표를 찾지 못하는 경우인데
# 아무래도 깊이 우선 탐색은 한 노드에 도착했을때, 갈 수 있는 모든 노드에 대해 고려하는 것이 먼저가 아닌
# 일단 왔던 방향으로 계속 간 후, 더 이상 갈 수 없을때, 다른 방향에 대한 고려를 하게 되는데,
# 이렇게 되면, 도착해야할 노드가 어려 방향이 아닌 다소 단순한 경로들로 이루어져 있다면 빠른 시간내에 찾을 수 있겠으나
# 가는데 간선이 여러개인 경우, 깊이가 엄청 깊어지면 재귀에 대한 제한 때문에 오버스택이 발생할 수도 있다.
# 따라서 최대한 빠르게 답을 찾기 위해선, 너비 우선 탐색으로 연결된 같은 깊이인 모든 노드에 대해 확인하면서
# 더 깊은 깊이로 나아가는게 재귀에 대한 오버스택이 발생하지도 않는 방법이다.
#
from collections import deque


def move_next(y, x, d):
    ny = (y + dy[d]) % R
    nx = (x + dx[d]) % C
    return ny, nx


def start_program(c_y, c_x, d, m):
    queue = deque()
    queue.append((c_y, c_x, d, m))
    while queue:
        c_y, c_x, d, m = queue.pop()
        visit_memory[d][m][c_y][c_x] = True
        command = command_list[c_y][c_x]
        if command == '@':
            return "YES"
        else:
            n_d = d
            if command == '>' or (command == '_' and not m):
                n_d = 1
            elif command == '<' or (command == '_' and m):
                n_d = 0
            elif command == 'v' or (command == '|' and not m):
                n_d = 3
            elif command == '^' or (command == '|' and m):
                n_d = 2
            elif command == '?':
                for i in range(4):
                    ncy, ncx = move_next(c_y, c_x, i)
                    if not visit_memory[i][m][ncy][ncx]:
                        queue.append((ncy, ncx, i, m))
            elif command == '.':
                pass
            elif command == '+':
                m = (m + 1) % 16
            elif command == '-':
                m = (m - 1) % 16
            else:
                m = int(command)
            ncy, ncx = move_next(c_y, c_x, n_d)
            if not visit_memory[n_d][m][ncy][ncx]:
                queue.append((ncy, ncx, n_d, m))
    return "NO"


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for T in range(int(input())):
    R, C = map(int, input().split())
    memory = 0
    visit_memory = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(16)] for _ in range(4)]
    command_list = [list(input().rstrip()) for _ in range(R)]
    print("#{} {}".format(T + 1, start_program(0, 0, 1, 0)))
