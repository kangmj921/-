def solution(v, n):
    global answer
    temp = []
    if n >= len(target_string):
        answer = len(v)
        return answer
    for i in range(len(v)):
        if v[i] + 1 < len(input_string) and input_string[v[i] + 1] == target_string[n]:
            temp.append(v[i] + 1)
    solution(temp, n + 1)
    return answer


for _ in range(10):
    T = int(input())
    target_string = input().rstrip('\n')
    input_string = input().rstrip('\n')
    visited, answer = [], 0
    for i in range(len(input_string)):
        if input_string[i] == target_string[0]:
            visited.append(i)
    solution(visited, 1)
    print("#{} {}".format(T, answer))
