def search(index):
    global answer
    visited[index] = 1
    for j in range(index, len(N)):
        temp = list(N)
        if not visited[j]:
            if index == 0 and N[j] == '0':
                continue
            elif N[index] == N[j]:
                continue
            else:
                temp[index], temp[j] = temp[j], temp[index]
                answer.append(int(''.join(temp)))
    if index + 1 < len(N):
        search(index + 1)


for T in range(int(input())):
    N = str(int(input()))
    visited = [0] * len(N)
    answer = [int(N)]
    for i in range(len(N)):
        search(i)
    print("#{} {} {}".format(T + 1, min(answer), max(answer)))