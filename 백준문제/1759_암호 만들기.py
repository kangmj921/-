def DFS(index, num_of_p, p):
    global password_list
    if num_of_p == L:
        password_list.append(p)
        return
    visited[index] = 1
    for i in range(index + 1, C):
        if not visited[i]:
            if p[-1] < possible_words[i]:
                DFS(i, num_of_p + 1, p + possible_words[i])
                visited[i] = 0


L, C = map(int, input().split())
possible_words = sorted(list(input().split()))
vowel_words = ['a', 'e', 'i', 'o', 'u']
password_list = []
for i in range(C):
    visited = [0] * C
    DFS(i, 1, possible_words[i])
remove_list = []
for word in password_list:
    count = 0
    for j in word:
        if j in vowel_words:
            count += 1
    if count == 0 or (count > L - 2):
        remove_list.append(word)
j = 0
for i in range(len(password_list)):
    if len(remove_list):
        if password_list[i] != remove_list[j]:
            print(password_list[i])
        else:
            if j < len(remove_list) - 1:
                j += 1
    else:
        print(password_list[i])