# 퍼즐을 맞추는 단계마다 저장해서 찾는 방법으로는 list나 queue로 찾는 것 보다는
# dict를 이용해서 하는 방법이 시간초과에 걸리지 않을 수 있다.
#
import math
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def swap(s, orig, target):
    a, b = s[orig], s[target]
    temp1 = s.replace(b, '@')
    temp2 = temp1.replace(a, b)
    temp3 = temp2.replace('@', a)
    return temp3


def search(c):
    global answer
    queue = deque()
    queue.append((''.join(''.join(board[i]) for i in range(3)), 0))
    while queue:
        puzzle_start, c = queue.popleft()
        if puzzle_start == correct_board:
            answer = min(answer, c)
        else:
            temp = puzzle_start.find('0')
            y = temp // 3
            x = temp % 3
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                    continue
                puzzle_next = swap(puzzle_start, temp, ny * 3 + nx)
                if not visit.get(puzzle_next):
                    visit[puzzle_next] = 1
                    queue.append((puzzle_next, c + 1))


board = [list(input().split()) for _ in range(3)]
correct_board = '123456780'
visit = dict()
answer = math.inf
search(0)
if answer == math.inf:
    answer = -1
print(answer)
