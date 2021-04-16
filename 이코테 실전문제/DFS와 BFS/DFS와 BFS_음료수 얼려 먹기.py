def solution(y, x):
    if y < 0 or y >= N or x < 0 or x >= M:
        return False
    if ice_frame[y][x] == 0:
        ice_frame[y][x] = 1
        solution(y + 1, x)
        solution(y - 1, x)
        solution(y, x - 1)
        solution(y, x + 1)
        return True
    return False
    pass


N, M = map(int, input().split())
ice_frame = []
result = 0
for i in range(N):
    ice_frame.append(list(map(int, input().rstrip('\n'))))
for i in range(N):
    for j in range(M):
        if solution(i, j):
            result += 1
print(result)
