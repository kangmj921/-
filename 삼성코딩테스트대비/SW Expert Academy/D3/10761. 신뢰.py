def search(B_idx, O_idx, time):  # 파랑 위치, 오렌지 위치, 시간
    while len(Blue) != 0 or len(Orange) != 0:
        # 파란색일 때,
        if robot_order[0] == 'B':
            # 현재 위치와 목표 값의 크기를 비교해서 이동
            if int(robot_order[1]) - 1 > B_idx:
                B_idx += 1
            elif int(robot_order[1]) - 1 < B_idx:
                B_idx -= 1
            # 목표 값에 도착하면
            # robot_order, Blue 값들 제거
            else:
                robot_order.pop(0)
                robot_order.pop(0)
                Blue.pop(0)
            # 오렌지 버튼도 눌러야 할 때,
            if len(Orange) != 0:
                if O_idx > Orange[0] - 1:
                    O_idx -= 1
                elif O_idx < Orange[0] - 1:
                    O_idx += 1
        else:
            if int(robot_order[1]) - 1 > O_idx:
                O_idx += 1
            elif int(robot_order[1]) - 1 < O_idx:
                O_idx -= 1
            else:
                robot_order.pop(0)
                robot_order.pop(0)
                Orange.pop(0)
            if len(Blue) != 0:
                if B_idx > Blue[0] - 1:
                    B_idx -= 1
                elif B_idx < Blue[0] - 1:
                    B_idx += 1
        time += 1
    return time


T = int(input())
for tc in range(1, 1 + T):
    robot_order = list(map(str, input().split()))
    # n 값
    n = int(robot_order.pop(0))
    Blue = []
    Orange = []
    # 파란색과 오렌지 색으로 분류
    for q in range(n):
        if robot_order[2 * q] == 'B':
            Blue.append(int(robot_order[2 * q + 1]))
        else:
            Orange.append(int(robot_order[2 * q + 1]))
    # 파랑 위치, 오렌지 위치, 시간
    print('#{} {}'.format(tc, search(0, 0, 0)))
