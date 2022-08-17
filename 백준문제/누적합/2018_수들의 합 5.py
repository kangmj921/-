# 투 포인터를 이용하여,
# 현재까지의 누적합이 N보다 작으면 오른쪽을 계속 늘려간다.
# 늘려가다가 N보다 커지게 되면 왼쪽 포인터를 오른쪽으로 늘린다.
# 포인터를 조작하는 와중에 누적합이 N이랑 같으면 가지수 + 1,
N = int(input())
s = 1
i, j = 1, 1
answer = 0
while True:
    if s < N:
        j += 1
        if j == N + 1:
            break
        s += j
    else:
        if s == N:
            answer += 1
        s -= i
        i += 1
print(answer)
