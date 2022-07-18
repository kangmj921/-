# 문제에서 헷갈린 부분과 착각한 부분이 있어서 시간이 조금 걸렸다.
# 구현 후 python3에선 시간초과가 걸리길래 최적화를 했다.
from collections import deque


def rotate_circle(circle_number, direction):
    temp = []
    if not direction:
        for idx in range(M):
            if idx == 0:
                temp.append(circle_num[circle_number][M - 1])
            else:
                temp.append(circle_num[circle_number][idx - 1])
    else:
        for idx in range(M):
            if idx == M - 1:
                temp.append(circle_num[circle_number][0])
            else:
                temp.append(circle_num[circle_number][idx + 1])
    return temp


def bfs_search(circle_number, j):
    d = [(1, 0), (0, -1), (0, 1)]
    global adjacent_same_num
    result = []
    queue = deque()
    visit_list = [[False] * M for _ in range(N + 1)]
    queue.append((circle_number, j))
    visit_list[circle_number][j] = True
    while queue:
        i, j = queue.popleft()
        for k in range(3):
            ni, nj = i + d[k][0], j + d[k][1]
            if nj < 0:
                nj = M - 1
            elif nj > M - 1:
                nj = 0
            if ni > N:
                continue
            if not visit_list[ni][nj] and circle_num[ni][nj] == circle_num[i][j]:
                visit_list[ni][nj] = True
                queue.append((ni, nj))
                if not result:
                    result = [(i, j), (ni, nj)]
                else:
                    result.append((ni, nj))
    adjacent_same_num += result
    return result


def to_zero(arr):
    for num, i in arr:
        circle_num[num][i] = 0


def sum_circle_num():
    result = 0
    for i in range(1, N + 1):
        result += sum(circle_num[i])
    return result


def average(t):
    for num in range(1, N + 1):
        for i in range(M):  # 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
            if circle_num[num][i] > t:
                circle_num[num][i] -= 1
            elif circle_num[num][i] and circle_num[num][i] < t:
                circle_num[num][i] += 1


N, M, T = map(int, input().split())
# 2 <= N, M <= 50  1 <= T <= 50
circle_num = [[]]
rotate_list = []

for i in range(1, N + 1):
    circle_num.append(list(map(int, input().split())))
# 0 = N, 1 = E, 2 = S, 3 = W
# 시계방향으로 돌릴경우, 오른쪽으로 회전하므로, 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
# 반시계방향일 경우는 그 반대, 0 -> 3, 3 -> 2, 2 -> 1, 1 -> 0
for i in range(T):  # 최대 50번 수행
    xi, di, ki = map(int, input().split())
# 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
    n = xi
    while n <= N:  # 최대 50번 수행
        # print(n, circle_num[n])
        for i in range(ki):
            circle_num[n] = rotate_circle(n, di)
        n += xi


# 인접한 수를 찾는 과정을 BFS로 구현하게 되면, 최대 (50 * 4) ^ 2 번 탐색 수행.
    adjacent_same_num = []
    total_circle, count = 0, 0
    for num in range(1, N + 1):
        for i in range(M):
            if circle_num[num][i]:  # 원판에 수가 남아있으면 인접하면서 수가 같은 것을 모두 찾는다.
                bfs_search(num, i)
                total_circle += circle_num[num][i]
                count += 1
    if adjacent_same_num:  # 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
        to_zero(adjacent_same_num)
    else:
        if count:
            total_circle /= count
        average(total_circle)
print(sum_circle_num())
