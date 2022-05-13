# 그리디한 방식으로 높이 별로 정렬한다음 가장 높은 박스에서 낮은 박스의 높이를 1개씩 dump하고
# 다시 정렬하는 방식으로 하였다. 정렬 1번의 시간 복잡도는 O(N)이고
# dump 횟수가 최대 1000이고 입력 받는 박스 줄의 개수가 100이므로
# 최대 O(100)*1000이기 때문에 그리디한 방식으로 하였다.
# 만약 입력 받는 박스의 줄의 개수나 dump 횟수가 더 많다면 다른 방식을 써야할 것이다.
#
for T in range(10):
    dump_num = int(input())
    height_list = sorted(list(map(int, input().split())))
    while dump_num > 0:
        height_list[-1] -= 1
        height_list[0] += 1
        dump_num -= 1
        height_list = sorted(height_list)  # 한 번 정렬하는데 O(N)임
    print("#{} {}".format(T + 1, height_list[-1] - height_list[0]))
