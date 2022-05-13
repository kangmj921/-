import sys


def DFS(c):
    global answer
    if not c:
        temp = int("".join(number_list))
        if answer < temp:
            answer = temp
        return
    for i in range(len(number_list)):
        for j in range(i + 1, len(number_list)):
            number_list[i], number_list[j] = number_list[j], number_list[i]
            temp = int("".join(number_list))
            if visited.get((temp, c - 1), 1):
                visited[(temp, c - 1)] = 0
                DFS(c - 1)
            number_list[i], number_list[j] = number_list[j], number_list[i]


for T in range(int(input())):
    answer = 0
    number_list, change_count = sys.stdin.readline().split()
    number_list = list(number_list)
    change_count = int(change_count)
    visited = {}
    DFS(change_count)
    print("#{} {}".format(T + 1, answer))
