# 추가 가능한 가로선 목록을 구현하는데 시간이 많이 걸렸다.
# 평소에 조합을 직접 구현해 봤으면, 금방 구현이 가능했을 것이다.

# 답안을 내보니, 메모리 초과가 걸렸다.
# 시간초과나 메모리 초과를 통과하기 위해선, 가로선의 조합을 구한 쪽을 건드려야 할 것 같다.
# 확인해보니 조합을 생성할때, 원소가 중복되는 경우가 있었다.
# 직접 조합을 구현하기 어려워 결국 combination을 썻다.

# 직접 조합을 구하니 시간 초과를 통과하기가 어려웠다. 우선 연결을 저장하던 리스트의
#
# from itertools import combinations
#
#
# # 모든 세로선에 대해 같은 세로선으로 갈 수 있는지 출발해봄.
# def check_ladder(ladder_added):  # 최대 H번 탐색함.
#     for y in range(1, N + 1):
#         i = 0
#         j = y
#         while i != H + 1:
#             if ladder_added[i + 1][j - 1]:
#                 i, j = i + 1, j - 1
#             elif ladder_added[i + 1][j]:
#                 i, j = i + 1, j + 1
#             else:
#                 i += 1
#         if j != y:
#             return False
#     return True
#
#
# # 필요한 가로선의 개수만큼, 추가할 수 있는 가로선의 조합 구함
# def check_possible_add(n, a):
#     for add_ladder in combinations(a, n):
#         for i in range(len(add_ladder)):
#             ladder[add_ladder[i][0]][add_ladder[i][1]] = 1
#         if check_ladder(ladder):
#             return True
#         else:
#             for i in range(len(add_ladder)):
#                 ladder[add_ladder[i][0]][add_ladder[i][1]] = 0
#     return False
#
#
# N, M, H = map(int, input().split())  # N은 최대 10, H는 최대 30
# ladder = [[0] * (N + 2) for _ in range(H + 2)]
# check = False
# # ladder 리스트의 최대 사이즈는 19 * 30 = 570
# for _ in range(M):
#     a, b = map(int, input().split())
#     ladder[a][b] = 1
# result = 0
# add_line = []
# for i in range(1, H + 1):
#     for j in range(1, N):
#         if not ladder[i][j]:
#             if j == 1:
#                 if N > 2 and ladder[i][j + 1]:
#                     continue
#             elif j == N - 1:
#                 if ladder[i][j - 1]:
#                     continue
#             else:
#                 if ladder[i][j - 1] or ladder[i][j + 1]:
#                     continue
#             add_line.append((i, j))
# while result < 4:  # 추가할 가로선을 1개부터 시작해서 임의의 위치에 넣어봄.
#     if result <= (N - 1) * H - M:
#         # 새로 추가할 가로선의 수만큼 남은 곳이 있는 지 체크한다.
#         if not check_possible_add(result, add_line):  # 세로선이 result 개 일때 i번 세로선의 결과가 i가 나오지 않으므로 1개 더 추가해봄.
#             result += 1
#         else:
#             break
# if result < 4:
#     print(result)
# else:
#     print(-1)

# 조합을 이용하지 않고 다른 방법으로 풀기..