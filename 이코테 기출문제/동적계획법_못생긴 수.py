# 못생긴 수는 2,3,5 만을 소인수로 가지는 수를 의미하므로,
# 2,3,5를 이미 소인수로 가지는 수에 또 2,3,5를 곱해서 수를 구하면
# 그 수는 2,3,5만을 소인수로 가지게 된다.
n = int(input())
num_list = [0] * n
num_list[0] = 1
i2, i3, i5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5
for i in range(1, n):
    num_list[i] = min(next2, next3, next5)
    if num_list[i] == next2:
        i2 += 1
        next2 = 2 * num_list[i2]
    if num_list[i] == next3:
        i3 += 1
        next3 = 3 * num_list[i3]
    if num_list[i] == next5:
        i5 += 1
        next5 = 5 * num_list[i5]
print(num_list[n-1])
