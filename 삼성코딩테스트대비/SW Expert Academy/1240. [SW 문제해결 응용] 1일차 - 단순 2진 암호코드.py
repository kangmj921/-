def check_password_code(p):
    even_digit, odd_digit = 0, 0
    for i in range(0, len(p), 2):
        odd_digit += p[i]
        even_digit += p[i + 1]
    if ((odd_digit * 3 + even_digit) % 10) != 0:
        return False
    else:
        return True


for T in range(int(input())):
    N, M = map(int, input().split())
    answer = 0
    password_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
                     '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
                     '0110111': 8, '0001011': 9}
    for _ in range(N):
        input_code = input()
        for j in range(len(input_code) - 1, 0, -1):
            if input_code[j] == '1':
                password_code = input_code[j - 55: j + 1]
                password = []
                for k in range(0, len(password_code), 7):
                    password.append(password_dict[password_code[k:k + 7]])
                if check_password_code(password):
                    answer = sum(password)
                else:
                    answer = 0
                break
    print("#{} {}".format(T + 1, answer))
