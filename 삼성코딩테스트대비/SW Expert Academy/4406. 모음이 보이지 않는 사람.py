for T in range(int(input())):
    answer = ''
    letter = input()
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for i in letter:
        if i not in vowel_list:
            answer += i
    print("#{} {}".format(T + 1, answer))
