# 현재 부분합 s가 S보다 길거나 크면 왼쪽 포인터가 가리키는 수를 빼ㄱ고
# 현재 j 와 i 사이의 값을 최소로 갱신한다.
# 현재 부분합 s가 S보다 작으면 오른쪽 포인터를 1 증가시킨다.
# j가 N일 경우 반복을 중지한다.
N, S = map(int, input().split())
N_list = list(map(int, input().split()))
s = N_list[0]
answer = 10 ** 12
i, j = 0, 0
while True:
    if s >= S:
        s -= N_list[i]
        answer = min(answer, j - i + 1)
        i += 1
    else:
        j += 1
        if j == N:
            break
        s += N_list[j]
print(0 if answer == 10 ** 12 else answer)
