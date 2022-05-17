# SWEA 사이트에 제출하면 총 3초의 실행시간이 걸리지만
# 파이참에선 30초 이상이 걸린다.
# 어떤 차이인지 알아야 할 것 같다.
import sys


def check_palindrome(s):
    for i in range(len(s) // 2):
        if s[len(s) - 1 - i] != s[i]:
            return False
    return True


for _ in range(10):
    T = int(input())
    letter_box = []
    answer = 1
    for _ in range(100):
        letter_box.append(sys.stdin.readline().rstrip('\n'))
    for palindrome_length in range(100, 3, -1):
        check = False
        for i in range(len(letter_box)):
            if check:
                break
            else:
                for j in range(len(letter_box[i]) - palindrome_length + 1):
                    temp1 = letter_box[i][j:j + palindrome_length]
                    if check_palindrome(temp1):
                        answer = max(answer, len(temp1))
                        check = True
                        break
                    temp2 = ""
                    for k in range(palindrome_length):
                        if j + k < len(letter_box):
                            temp2 += letter_box[j + k][i]
                    if check_palindrome(temp2):
                        answer = max(answer, len(temp2))
                        check = True
                        break
    print("#{} {}".format(T, answer))
