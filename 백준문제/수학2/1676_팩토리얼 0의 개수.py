N = int(input())
answer = 0
dp_list = [1]
for i in range(2, N + 1):
    dp_list.append(dp_list[-1] * i)
target = str(dp_list[-1])
j = len(target) - 1
while target[j] == '0':
    answer += 1
    j -= 1
print(answer)
