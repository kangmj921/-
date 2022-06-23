# 테트리스 하듯이 장식판을 주어진 순서대로 상자에 높이를 넘지 않게 쌓을 수 있는지 확인하고
# 넘을 경우 새 박스에 넣는다. 그리고 다 넣은 후 상자에 채워진 만큼의 높이들을 구하면 되는 문제이다.
# 구현을 간단히 할 방법이 있는지 좀 더 생각해봐야겠다.
# 구현을 모두 마쳤는데, 반레를 찾아봐야한다.
# 좀 더 간단한 방법으로 구현해서 반례를 찾기 수월하게 하려고한다.

# 기존의 방법은 테트리스와 같은 방식으로 장식판이 채워진 상자 높이 바로 다음에서
# 부터 내려와서 상자의 높이를 넘지 않게 채울 수 있는지로 구현하였는데
# 채울 수 있는지 확인하는 과정에서 박스의 높이를 지정하는 인덱스나 장식판의 높이를 지정하는
# 인덱스 등 지정하기 까다로웠다.

# 그래서 각 장식판의 저장을 다르게 하기로 했다.
# 각 장식판은 h * w의 리스트로 표현되는게 아닌 2차원 리스트로 표현되며
# 해당 너비에 존재하는 장식판의 제일 높은 부분의 빈 곳의 수, 제일 낮은 곳의 빈 곳의 수를 나타낸다.
# 예를 들어, ['XXX..', '..X..', '..XXX', '..X..']로 나타냈던 장식판을
# [0, 0, 0, 2, 2], [2, 2, 0, 1, 1]로 나타낸다. 각 인덱스는 너비에 해당하는 인덱스.
# 값은 너비 인덱스에서 제일 높은 높이와 낮은 높이를 나타낸 값이다.
# 이제 장식판을 쌓을때, 제일 마지막에 쌓은 장식판의 높은 부분을 나타낸 리스트와
# 쌓을 장식판의 제일 낮은 부분을 나타낸 리스트와 비교를 한다.
# 예를 들어, ['XXXXX', '.XXXX', '..XXX', '...XX', '....X']의 장식판 위에
# 아까 예시로 든 장식판을 쌓는 상황일떄, [0, 0, 0, 0, 0] 위에 [3, 3, 0, 1, 1]를 쌓는다.
# 두 리스트를 합하게 되면, [3, 3, 0, 1, 1]이 나오고 이 중 최소값은 0이 나오는데,
# 0만큼 위에 쌓은 장식판이 밑으로 내려갔다는 것을 말한다. 즉 바로 위에 쌓았다는 의미이다.
#
# 빈 곳에 맞게 채워지는 경우 : ['XXX..', '..X..', '..XXX', '..X..'] 위에
# ['XXXXX', '.XXXX', '..XXX', '...XX', '....X']가 오는 경우
# [0, 0, 0, 2, 2]와 [4, 3, 2, 1, 0]합은 [4, 3, 2, 3, 2] 최솟값은 2
# 2만큼 장식판이 밑으로 이동해서 쌓였다는 뜻이다.
# 그리고 기록해둔 쌓인 장식판의 높이와 새로 쌓을 장식판의 높이 - 밑으로 이동해서 쌒은 높이를 구하고
# 해당 구한 값이 b보다 크면 새로 박스를 장만해서 새로 쌓고 높이를 기록한다.
# 결과 맞음!
#
# ............................실패했던 풀이..........................
# def check_all_height(d, b_idx):
#     check = True
#     c = 0
#     for i in range(len(d) - 1, -1, -1):
#         if check:
#             for j in range(w):
#                 if b_idx + c >= b:
#                     return False
#                 else:
#                     if d[i][j] == 'X' and box_list[b_idx + c][j] == 'X':
#                         return False
#         c += 1
#     return check
#
#
# def check_decorate_put(d, b_idx):
#     start = b_idx
#     temp = -1
#     while 0 <= start <= b:
#         # print(start)
#         if check_all_height(d, start):
#             temp = start
#             start -= 1
#         else:
#             if temp >= 0:
#                 return temp
#             else:
#                 start -= 1
#     return temp
#
#
# def solve_1():
#     box_list = [['.'] * w for _ in range(b)]
#     box_index = 0
#     box_add = False
#     idx = 0
#     while idx < n:
#         decorate_height = len(decorate_list[idx])
#         to_check_list = decorate_list[idx]
#         if not box_index:
#             for h in range(decorate_height):
#                 box_list[h] = to_check_list[decorate_height - 1 - h]
#             box_index += decorate_height
#             idx += 1
#         else:
#             max_box_height = check_decorate_put(to_check_list, box_index)  # 새로 장식판을 집어 넣을때 최대 넣을 수 있는 높이
#             # print(max_box_height)
#             if max_box_height == -1:
#                 box_add = True
#             else:
#                 if max_box_height + decorate_height > b:
#                     box_add = True
#                 else:
#                     c = 1
#                     for i in range(max_box_height, max_box_height + decorate_height):
#                         for j in range(w):
#                             if box_list[i][j] == '.' and to_check_list[decorate_height - c][j] == 'X':
#                                 box_list[i][j] = 'X'
#                         c += 1
#                     box_index = max_box_height + decorate_height
#                     idx += 1
#         if box_add:
#             answer.append(box_index)
#             box_index = 0
#             box_list = [['.'] * w for _ in range(b)]
#     if box_index:
#         answer.append(box_index)
#     print(*answer)


n, w, b = map(int, input().split())  # n은 장식판의 종류, w는 장식판과 박스의 너비,
# b는 박스의 높이
answer = []
decorate_list = []
top_bottom_list = []
h_list = []
for i in range(n):
    h = int(input())  # 장식판의 높이
    h_list.append(h)
    decorate_list.append([list(input().rstrip()) for _ in range(h)])
for decorate in decorate_list:
    top, bottom = [], []
    for i in range(w):
        count = 0
        for j in range(len(decorate)):
            if decorate[j][i] == '.':
                count += 1
            else:
                break
        top.append(count)
    for i in range(w):
        count = 0
        for j in range(len(decorate) - 1, -1, -1):
            if decorate[j][i] == '.':
                count += 1
            else:
                break
        bottom.append(count)
    top_bottom_list.append([top, bottom])
for i in range(len(top_bottom_list)):
    if not i:
        present_height = h_list[0]
    else:
        prev_top = top_bottom_list[i - 1][0]
        pres_bottom = top_bottom_list[i][1]
        result = []
        for j in range(w):
            result.append(prev_top[j] + pres_bottom[j])
        move_down_height = min(result)
        if present_height + h_list[i] - move_down_height > b:
            answer.append(present_height)
            present_height = h_list[i]
        else:
            present_height += h_list[i] - move_down_height
if present_height:
    answer.append(present_height)
print(*answer)
