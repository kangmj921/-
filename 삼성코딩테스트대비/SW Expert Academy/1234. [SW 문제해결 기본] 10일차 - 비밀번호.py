for T in range(10):
    N, p_string = input().split()
    p_string = list(p_string)
    stack = [0]
    while True:
        temp = "".join(p_string)
        for i in range(1, len(p_string)):
            if p_string[i] == p_string[i - 1]:
                del p_string[i - 1: i + 1]
                break
        if "".join(p_string) == temp:
            break
    print("#{} {}".format(T + 1, "".join(p_string)))
