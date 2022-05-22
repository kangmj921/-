for T in range(int(input())):
    input_s = input()
    answer = 0
    total_people = 0
    for need_people, people in enumerate(input_s):
        if need_people <= total_people:
            total_people += int(people)
        else:
            answer += need_people - total_people
            total_people += need_people - total_people + int(people)
    print("#{} {}".format(T + 1, answer))
