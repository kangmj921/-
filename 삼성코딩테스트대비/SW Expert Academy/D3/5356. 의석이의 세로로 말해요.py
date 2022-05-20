for T in range(int(input())):
    letter_list, index = [], 0
    answer = ''
    for _ in range(5):
        letter_list.append(input().rstrip('\n'))
    while True:
        temp = ''
        for i in range(5):
            if index < len(letter_list[i]):
                temp += letter_list[i][index]
            else:
                temp += ''
        answer += temp
        index += 1
        if temp == '':
            break
    print("#{} {}".format(T + 1, answer))
