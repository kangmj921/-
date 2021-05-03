import sys

num_list = []
mode_list = []
for _ in range(int(input())):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
average = int(round(sum(num_list) / len(num_list), 0))
mid = num_list[len(num_list) // 2]
range = num_list[-1] - num_list[0]
for i in num_list:
    if len(mode_list) == 0:
        mode_list.append((i, 1))
    else:
        if mode_list[-1][0] == i:
            value, count = mode_list.pop()
            mode_list.append((value, count + 1))
        else:
            mode_list.append((i, 1))
mode_list.sort(reverse=True, key=lambda x : x[1])
if len(mode_list) > 1 and mode_list[0][1] == mode_list[1][1]:
    mode = mode_list[1][0]
else:
    mode = mode_list[0][0]
print(average)
print(mid)
print(mode)
print(range)
