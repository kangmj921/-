import sys


def wild_card(name_list, Wild_card):
    for t in range(len(name_list)):
        char_index = 0
        if visit_list[t]:
            for k in range(len(Wild_card)):
                if Wild_card[k] == '*':
                        char_index = match(k, name_list[t], Wild_card)
                        if not char_index:
                            visit_list[t] = False
                elif Wild_card[k] == '?':
                    if name_list[t][char_index] == '!':
                        visit_list[t] = False
                    char_index += 1
                else:
                    if Wild_card[k] != name_list[t][char_index]:
                        visit_list[t] = False
                    char_index += 1
    print(visit_list)
    for j in range(len(visit_list)):
        if visit_list[j]:
            word_list.append(name_list[j][:-1])
    return


def match(start, word, Wild_card):
    end = Wild_card[start+1:].index('*') + start + 1
    pattern = Wild_card[start+1:end]
    word = "".join(word)
    print(pattern)
    return


def check_wild_card(Wild_card):
    i = 0
    while Wild_card[i] != '!':
        if Wild_card[i] == '*' and Wild_card[i + 1] == '*':
            del Wild_card[i]
        else:
            i += 1
    return Wild_card

if __name__ == '__main__':
    for C in range(int(input())):
        W = list(sys.stdin.readline().rstrip('\n') + '!')
        W = check_wild_card(W)
        word_list = list()
        file_name = list()
        for N in range(int(input())):
            file_name.append(list(sys.stdin.readline().replace('\n', '!')))
        visit_list = [True for k in range(len(file_name))]
        wild_card(file_name, W)
        word_list.sort()
        for i in range(len(word_list)):
            print("".join(word_list[i]))
