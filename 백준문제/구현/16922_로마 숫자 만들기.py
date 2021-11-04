# DFS를 이용해서 모든 경우에 대해 탐색을 진행하면서, 이미 만들어진 숫자를
# 탐색에서 제외하면서 결과를 구할 수 있도록 한다.
# 10개의 문자를 사용할 때, 0~9개의 문자를 사용한 경우는 기록하지 않도록한다.
# 백트래킹(N개의 숫자를 4개의 문자로 구성), 조합을 이용하여서도 구현할 수 있다.
N = int(input())
visited = [0] * 1001
Num_by_letter = [1, 5, 10, 50]
result = 0


def dfs(depth, start, num):
    global result
    if depth == N:
        if visited[num] == 0:
            result += 1
            visited[num] = 1
    else:
        for i in range(start, 4):
            num += Num_by_letter[i]
            dfs(depth + 1, i, num)
            num -= Num_by_letter[i]


dfs(0, 0, 0)
print(result)
