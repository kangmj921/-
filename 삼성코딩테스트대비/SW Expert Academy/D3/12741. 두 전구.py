T = int(input())
answer = []
for _ in range(T):
    A, B, C, D = map(int, input().split())
    result = min(B, D) - max(A, C)
    if result > 0:
        answer.append(result)
    else:
        answer.append(0)
for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))
