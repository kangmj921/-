def check_palindrome(s):
    for i in range(len(s) // 2):
        if s[len(s) - 1 - i] != s[i]:
            return False
    return True


for T in range(10):
    palindrome_length = int(input())
    letter_box = []
    answer = 0
    for _ in range(8):
        letter_box.append(list(input().rstrip('\n')))
    for i in range(len(letter_box)):
        temp1 = ""
        for j in range(len(letter_box[i]) - palindrome_length + 1):
            temp1 = "".join(letter_box[i][j:j+palindrome_length])
            if check_palindrome(temp1):
                answer += 1
            temp2 = ""
            for k in range(palindrome_length):
                temp2 += letter_box[j + k][i]
            if check_palindrome(temp2):
                answer += 1
    print("#{} {}".format(T + 1, answer))
