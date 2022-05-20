for tc in range(10):
    N = int(input())
    password = list(input().split())
    num_of_command = int(input())
    command = list(input().split())
    temp = ['I', 'D', 'A']
    i = 0
    while i < len(command):
        if command[i] in temp:
            if command[i] == 'I':
                x, y = int(command[i + 1]), int(command[i + 2])
                a = i + 3
                while a < len(command) and (command[a] not in temp):
                    a += 1
                s = command[i + 3:a]
                for j in range(y):
                    password.insert(x + j, s[j])
                i = a
            elif command[i] == 'D':
                x, y = int(command[i + 1]), int(command[i + 2])
                i += 3
                for _ in range(y):
                    password.pop(x + 1)
            else:
                y = command[i + 1]
                c = i + 2
                while c < len(command) and (command[c] not in temp):
                    c += 1
                s = command[i + 2:c]
                i = c
                password.append(" ".join(s))
    print("#{} {}".format(tc + 1, " ".join(password[:10])))
