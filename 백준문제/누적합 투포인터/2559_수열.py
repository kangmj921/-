# 길이 K인 슬라이딩 윈도우를 이용해서 푸는 문제이다.

N, K = map(int, input().split())
N_list = list(map(int, input().split()))
i, j = 0, K - 1
result = sum(N_list[:K])
answer = result
while True:
    j += 1
    if j == N:
        break
    result += N_list[j]
    result -= N_list[i]
    i += 1
    answer = max(answer, result)
print(answer)
