# 앞선 연구소와 비슷하게 풀 수 있는 문제.
def combination_to_3(list):
    result_list = []
    for i in range(0, len(list) - 2):
        for j in range(i+1, len(list) - 1):
            for k in range(j+1, len(list)):
                result_list.append([list[i], list[j], list[k]])
    return result_list


def check_student(list, start_point):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        y, x = start_point
        while True:
            next_x = x + dx[i]
            next_y = y + dy[i]
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                break
            if list[next_y][next_x] == 'S':
                return False
            if list[next_y][next_x] == 'O':
                break
            y, x = next_y, next_x
    return True


def check_process(c, t):
    for i in t:
        if not check_student(c, i):
            return False
    return True


N = int(input())
corridor_map = []
for i in range(N):
    corridor_map.append(list(input().split()))
obstacle_list = []
teacher_list = []
for i in range(N):
    for j in range(N):
        if corridor_map[i][j] == 'X':
            obstacle_list.append((i, j))
for i in range(N):
    for j in range(N):
        if corridor_map[i][j] == 'T':
            teacher_list.append((i, j))
choice_3_obstacle = combination_to_3(obstacle_list)
check = False
for [a, b, c] in choice_3_obstacle:
    corridor_map[a[0]][a[1]], corridor_map[b[0]][b[1]], corridor_map[c[0]][c[1]] = 'O', 'O', 'O'
    if check_process(corridor_map, teacher_list):
        check = True
        break
    corridor_map[a[0]][a[1]], corridor_map[b[0]][b[1]], corridor_map[c[0]][c[1]] = 'X', 'X', 'X'
if check:
    print("YES")
else:
    print("NO")
