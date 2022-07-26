# 배열의 최대 크기가 2^30으로, 전체 배열을 탐색하며 수를 찾으면 매우 큰 복잡도를 가진다.
# 따라서 필요한 곳만 탐색하기 위해 분할 정복을 사용하여
# 큰 z를 제일 작은 z로 분할하는 과정을 거칠 것이다.
# 이 때, 분할하는 과정에서 찾을 r, c가 포함된 z만 탐색하고
# 나머지 z는 안에 들어있는 수를 고려하지 않고 해당 z의 변의 제곱을 한 번에 계산해서
# 다음 z에서 시작하는 수를 구한다.
# z의 범위 안에 r, c가 있을 경우, 2로 나눈 값을 변의 수로 가지는 z를 다시 탐색한다.
# 결국 n이 2와 같거나 작게 되면, 가장 작은 z이다.
# 이 떄, r, c에 따라 값을 구할 수 있다.
result = 0


def search(n, y, x):
    global result
    if not (y <= r < y + n and x <= c < x + n):
        result += n * n
        return
    if n > 2:
        search(n // 2, y, x)
        search(n // 2, y, x + n // 2)
        search(n // 2, y + n // 2, x)
        search(n // 2, y + n // 2, x + n // 2)
    else:
        if y == r and x == c:
            print(result)
        elif y == r and x + 1 == c:
            print(result + 1)
        elif y + 1 == r and x == c:
            print(result + 2)
        else:
            print(result + 3)


N, r, c = map(int, input().split())
search(2 ** N, 0, 0)
