#  BFS를 활용하는 문제인데, 죄수 2명이 모두 탈출하는 최소의 값을 어떻게 찾을지 고민된다.
#  일단 각각 순차적으로 하게 되면, 각각의 경로에 대해 문인 부분을 열고 진행을 해야 하는데
#  출구가 여러개고, 그 출구 각각에 대한 경로가 여러개가 되면 풀이가 복잡해진다.
#  일단 각 죄수에 대해 모든 탈출구에 대해 문의 개수가 몇개인지 살펴본다.
#  그리고 2명의 죄수가 각각 독립적으로 출구에 대한 문의 개수를 알아보고 나중에
#  합쳐서 어떻게 최소의 문 수를 구할 지 구하는 방법도 어렵다.
#  다른 풀이를 보니 밖의 제 3자를 도입해서, 제 3자가 각 죄수에게 가는 최소 벽의 개수를
#  구한 뒤, 각 죄수가 여는 문 수를 구한 것들과 합하고 중복되서 열어진 횟수만 큼
#  빼면 결국 구하는 최소의 문 개수를 구할 수 있다고 한다.
#  제 3자를 도입했을시, 감옥 밖으로 1줄씩 테두리를 추가해서 모든 출구에서 부터 깊이 우선
#  탐색으로 각 지점 별 최소의 문의 개수를 알 수 있다.
#  그리고 제3자와 죄수 두명과 함께 만나는 지점 중 최소의 값을 가지는 지점이 곧 탈출하기
#  위한 최소의 문 개수이다.
#  문제 자체의 코드는 이해하기 어렵지 않았지만, 이 최소 문 개수를 구하기 위해 제 3자를 써야하고
#  이 3명이 만나는 지점을 구해야하는 등 플 4 문제 답게 일반적인 생각으론 구하기 어려운
#  문제였다.

import sys
from collections import deque
import math


def BFS(s):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    queue = deque()
    queue.append(s)
    visited[s[0]][s[1]] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= h + 2 or nx < 0 or nx >= w + 2:
                continue
            if visited[ny][nx] == -1:
                if jail_inf[ny][nx] == '#':
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))
                elif jail_inf[ny][nx] == '.' or jail_inf[ny][nx] == '$':
                    visited[ny][nx] = visited[y][x]
                    queue.appendleft((ny, nx))
    return visited


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for T in range(int(input())):
    h, w = map(int, input().split())
    jail_inf = [list('.' + sys.stdin.readline().rstrip() + '.') for _ in range(h)]
    jail_inf.append(['.'] * (w + 2))
    jail_inf.insert(0, ['.'] * (w + 2))
    stack, answer = [], math.inf
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if jail_inf[i][j] == '$':
                stack.append((i, j))
    answer_1 = BFS(stack[0])
    answer_2 = BFS(stack[1])
    answer_3 = BFS((0, 0))
    for i in range(h + 2):
        for j in range(w + 2):
            if answer_1[i][j] != -1 and answer_2[i][j] != -1 and answer_3[i][j] != -1:
                result = answer_1[i][j] + answer_2[i][j] + answer_3[i][j]
                if jail_inf[i][j] == '.':
                    continue
                if jail_inf[i][j] == '#':
                    result -= 2
                print(result, i, j)
                answer = min(answer, result)
    print(answer)
