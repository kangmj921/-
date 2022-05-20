for _ in range(10):
    T = int(input())
    array_list = []
    x_max, y_max, diag_max1, diag_max2 = 0, 0, 0, 0
    for _ in range(100):
        array_list.append(list(map(int, input().split())))
    for i in range(len(array_list)):
        temp1, temp2, temp3, temp4 = 0, 0, 0, 0
        for j in range(len(array_list[i])):
            temp1 += array_list[i][j]
            temp2 += array_list[j][i]
            temp3 += array_list[j][j]
            temp4 += array_list[j][len(array_list[i]) - 1 - j]
        x_max = max(x_max, temp1)
        y_max = max(y_max, temp2)
        diag_max1 = max(diag_max1, temp3)
        diag_max2 = max(diag_max2, temp4)
    print("#{} {}".format(T, max(x_max, y_max, diag_max1, diag_max2)))
