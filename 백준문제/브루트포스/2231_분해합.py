N = int(input())
answer = []
for i in range(1, N + 1):
    result = i + sum(list(map(int, str(i))))
    if result == N:
        answer.append(i)
if not answer:
    print(0)
else:
    print(answer[0])
