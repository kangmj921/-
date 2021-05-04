N = int(input())
num_list = list(map(int, input().split()))
sort_num_list = sorted(num_list)
stack = []
count = 0
dict = {

}
for i in sort_num_list:
    if len(stack) == 0:
        dict[i] = count
    else:
        if stack[-1] < i:
            count += 1
            dict[i] = count
    stack.append(i)
for i in num_list:
    print(dict[i], end=" ")
