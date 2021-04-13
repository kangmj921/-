H, W = map(int, input().split())
height_list = list(map(int, input().split()))
result = 0
for i in range(1, W - 1):
    left_height = height_list[i]
    for j in range(i - 1, -1, -1):
        if height_list[j] > left_height:
            left_height = height_list[j]
    right_height = height_list[i]
    for k in range(i + 1, W):
        if height_list[k] > right_height:
            right_height = height_list[k]
    final_height = min(left_height, right_height)
    result += final_height - height_list[i]
print(result)
