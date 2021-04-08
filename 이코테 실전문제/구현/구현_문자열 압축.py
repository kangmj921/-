import sys


def solution(char, string):
    global result_data
    answer = 1
    result = ''
    for i in range(len(char), len(string)+1, len(char)):
        #print(char)
        if string[i:i+len(char)] == char:
            answer += 1
        else:
            if answer > 1:
                result += str(answer) + char
            else:
                result += char
            char = string[i:i+len(char)]
            answer = 1
    result_data.append(result+string[i:])
    #print(result_data)


input_data = sys.stdin.readline().rstrip('\n')
result_data = []
a = ''
for i in input_data:
    a += i
    solution(a, input_data)
print(len(min(result_data, key=len)))
