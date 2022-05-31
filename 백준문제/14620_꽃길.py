# 재귀함수를 쓸때, 주의해서 쓰자
# 첫 번째 선택된 씨앗이 꼭 최적의 값일 수는 없으므로 이 값을 나중에 잘 빼줘서
# 완전탐색이 가능하게 해주는게 중요하다.
def search(n, total, v):
    global answer
    if n == 3:
        answer = min(answer, total)
        return
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if not v[i][j] and not v[i + 1][j] and not v[i - 1][j] \
                    and not v[i][j - 1] and not v[i][j + 1]:
                v[i][j], v[i + 1][j], v[i - 1][j], v[i][j + 1], v[i][j - 1]\
                    = True, True, True, True, True
                search(n + 1, total + (price_list[i][j] + price_list[i + 1][j]
                                             + price_list[i - 1][j] + price_list[i][j + 1]
                                             + price_list[i][j - 1]), v)
                v[i][j], v[i + 1][j], v[i - 1][j], v[i][j + 1], v[i][j - 1] \
                    = False, False, False, False, False


answer = 9999
N = int(input())
price_list = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
search(0, 0, visited)
print(answer)
