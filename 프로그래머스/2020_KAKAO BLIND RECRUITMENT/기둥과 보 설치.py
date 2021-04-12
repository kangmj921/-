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