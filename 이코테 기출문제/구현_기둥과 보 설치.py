import sys


# a는 설치할 구조물의 종류, 0:기둥, 1:보
# b는 행동의 종류, 0:삭제, 1:설치
# 구조물을 겹치게 설치하거나 없는 구조물을 삭제하는 경우는 입력으로 주어지지않음
# 바닥에 보를 설치하거나 벽면을 벗어나게 기둥,보를 설치하는 경우를 없도록


def check_frame(r):
    for x, y, stuff in r:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in r or [x, y, 1] in r or [x, y - 1, 0] in r:
                continue
            return False
        else:
            if [x, y - 1, 0] in r or [x + 1, y - 1, 0] in r or ([x-1, y, 1] in r and [x+1, y, 1] in r):
                continue
            return False
    return True


def solution(n, build_frame):
    result = []
    for x, y, stuff, action in build_frame:
        if action == 1:  # 설치할 때
            if 0 <= x <= n and 0 <= y <= n:
                result.append([x, y, stuff])
                if not check_frame(result):
                    result.remove([x, y, stuff])
        else:  # 삭제할 때
            if 0 <= x <= n and 0 <= y <= n:
                result.remove([x, y, stuff])
                if not check_frame(result):
                    result.append([x, y, stuff])
    result.sort(key=lambda k: (k[0], k[1], k[2]))
    return result


N = 5
# b_f = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
#        [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# b_f = [[0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1], [2, 2, 1, 1]]
b_f = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
       [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
       [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(N, b_f))
