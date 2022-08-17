# 투 포인터를 활용하는 문제이다.
# 순서 상관없이 2개의 수만 뽑아 합이 M이 되도록 하면 된다.
# 따라서 정렬 해놓고 오른쪽에서 시작한 수 + 왼쪽에서 시작한 수로 해서
# 합이 M보다 작으면 왼쪽의 인덱스를 증가시키고, 크면 오른쪽의 인덱스를 감소시키는 식으로
# 합이 M인 두 수의 조합이 몇 개 인지 찾는다.
N = int(input())
M = int(input())
N_list = sorted(list(map(int, input().split())))
i, j = 0, N - 1
answer = 0
while i < j:
    result = N_list[i] + N_list[j]
    if result < M:
        i += 1
    else:
        if result == M:
            answer += 1
        j -= 1
print(answer)
