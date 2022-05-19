def DFS(index, total):
    global answer
    total += A[index]
    visited[index] = 1
    if total == K:
        answer += 1
    for i in range(index, N):
        if not visited[i]:
            DFS(i, total)
            visited[i] = 0


for T in range(int(input())):
    answer = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [0] * N
    for i in range(N):
        DFS(i, 0)
    print("#{} {}".format(T + 1, answer))
