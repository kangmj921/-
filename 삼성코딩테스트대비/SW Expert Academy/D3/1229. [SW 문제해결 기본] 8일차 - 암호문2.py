for tc in range(10):
    N = int(input())
    password = list(input().split())
    num_of_command = int(input())
    command = list(input().split())
    temp = ['I', 'D']
    i = 0
    while i < len(command):
        if command[i] in temp:
            x, y = int(command[i + 1]), int(command[i + 2])
            if command[i] == 'I':
                a = i + 3
                while a < len(command) and (command[a] not in temp):
                    a += 1
                s = command[i + 3:a]
                for j in range(y):
                    password.insert(x + j, s[j])
                i = a
                continue
            if command[i] == 'D':
                i += 3
                for _ in range(y):
                    password.pop(x)
                continue
    print("#{} {}".format(tc + 1, " ".join(password[:10])))
