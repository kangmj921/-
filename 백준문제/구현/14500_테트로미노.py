result_list = [0]


# DFS 방식으로 구현을 하고 싶었는데, 아직 DFS를 구현하는 실력이 부족한 것 같다.
# 추후에 DFS 공부후에 다시 풀어야겠다..
def solution(point_list, v):
    y, x = point_list[-1][0], point_list[-1][1]
    v[y][x] = 1
    print(point_list)
    if x >= M or y >= N:
        return None
    if len(point_list) == 4:
        result = 0
        for y, x in point_list:
            result += num_list[y][x]
        if result > result_list[-1]:
            result_list[-1] = result
        return None
    else:
        nx, ny = x + 1, y + 1
        px, py = x - 1, y - 1


N, M = map(int, input().split())
num_list = []
visited = [[0] * M for i in range(N)]
for i in range(N):
    num_list.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        solution([(j, i)], visited)
print(result_list[-1])
