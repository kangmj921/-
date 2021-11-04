def print_key(op, index):
    return op.replace(op[index], '[' + op[index] + ']', 1)


N = int(input())
key_list = []
for i in range(N):
    option = input().rstrip('\n')
    if option[0] not in key_list:
        key_list.append(option[0])
        print(print_key(option, 0))
    else:
        option_by_word = option.split()
