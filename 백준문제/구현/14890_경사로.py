def check(y, x, c):
    visit = [0] * N
    count = 1
    stack = []
    if c == 'r':  # 행에 대해서 탐색.
        for i in range(N):
            if not stack:
                stack.append(map_list[y][i])
            else:
                if stack[-1] == map_list[y][i]:
                    count += 1
                elif map_list[y][i] - stack[-1] == 1:
                    if count >= L and visit[i - L:i] == [0] * L:
                        visit[i - L:i] = [1] * L
                        stack.append(map_list[y][i])
                        count = 1
                    else:
                        return False
                elif stack[-1] - map_list[y][i] == 1:
                    if i + L <= N:
                        if map_list[y][i:i + L] == [stack[-1] - 1] * L and visit[i:i + L] == [0] * L:
                            visit[i:i + L] = [1] * L
                            stack.append(map_list[y][i])
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
    if c == 'c':  # 열에 대해서 탐색.
        for i in range(N):
            if not stack:
                stack.append(map_list[i][x])
            else:
                if stack[-1] == map_list[i][x]:
                    count += 1
                elif map_list[i][x] - stack[-1] == 1:  # 올라가는 경사면 놓을 때
                    if count >= L and visit[i - L:i] == [0] * L:
                        visit[i - L:i] = [1] * L
                        stack.append(map_list[i][x])
                        count = 1
                    else:
                        return False
                elif stack[-1] - map_list[i][x] == 1:  # 내려오는 경사면 놓을 때
                    temp = []
                    if i + L <= N:
                        for j in range(i, i + L):
                            temp.append(map_list[j][x])
                    else:
                        return False
                    if temp == [stack[-1] - 1] * L and visit[i:i + L] == [0] * L:
                        visit[i:i + L] = [1] * L
                        stack.append(map_list[i][x])
                    else:
                        return False
                else:
                    return False
    # print(y, x)
    return True


N, L = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for i in range(N):
    if check(i, 0, 'r'):  # 행에 대해서 길이 되는지 탐색
        answer += 1
    if check(0, i, 'c'):  # 열에 대해서 길이 되는지 탐색
        answer += 1
print(answer)
