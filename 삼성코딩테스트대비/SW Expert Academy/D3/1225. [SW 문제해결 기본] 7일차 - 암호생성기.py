while True:
    temp_input = input()
    if temp_input != '':
        T = int(temp_input)
    else:
        exit()
    data_list = list(map(int, input().split()))
    i = 1
    while True:
        first_data = data_list.pop(0)
        if i > 5:
            i = 1
        if first_data - i <= 0:
            data_list.append(0)
            break
        else:
            data_list.append(first_data - i)
        i += 1
    print("#{} {}".format(T, " ".join(map(str, data_list))))
