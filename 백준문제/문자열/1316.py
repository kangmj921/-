N = int(input())
result = N
for k in range(N):
    word = input()
    n = len(word)
    check_group_word = list(set(word))
    for t in range(len(check_group_word)):
        char_first_position = word.find(check_group_word[t])
        find_next_position = char_first_position + 1
        while word.find(check_group_word[t], find_next_position) == find_next_position and find_next_position < n:
            find_next_position += 1
        if word.find(check_group_word[t], find_next_position) > find_next_position:
            result -= 1
            break
        else:
            result += 0
print(result)