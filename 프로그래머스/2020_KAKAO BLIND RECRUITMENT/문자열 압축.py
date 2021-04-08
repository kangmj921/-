def solution(s):
    result_data = []
    a = ''
    for i in s:
        a += i
        answer = 1
        result = ''
        char = a
        for i in range(len(char), len(s)+1, len(char)):
            if s[i:i+len(char)] == char:
                answer += 1
            else:
                if answer > 1:
                    result += str(answer) + char
                else:
                    result += char
                char = s[i:i+len(char)]
                answer = 1
        result_data.append(result+s[i:])
    return len(min(result_data, key=len))