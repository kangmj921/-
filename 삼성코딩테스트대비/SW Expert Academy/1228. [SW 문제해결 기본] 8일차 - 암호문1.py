for T in range(10):
    N = int(input())
    password = list(map(str, input().split()))
    num_of_com = int(input())
    input_command = list(map(str, input().split('I ')))
    command_list = []
    for i in range(1, len(input_command)):
        command_list.append(input_command[i].split())
    for i in range(len(command_list)):
        x, y = map(int, command_list[i][:2])
        for j in range(y):
            password.insert(x + j, command_list[i][2 + j])
    print("#{} {}".format(T + 1, " ".join(password[:10])))
