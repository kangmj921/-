# N 개의 카드를 뽑는 최댓값은, N - i 개 뽑은 값 + i개 뽑은 값들 중 최댓값이다.
# N이 최대 1000이므로, O(N*N)으로도 풀 수 있다.
N = int(input())
Price_list = [0] + list(map(int, input().split()))
dp_list = [0] * (N + 1)
dp_list[1] = Price_list[1]
for i in range(2, N + 1):  # 최대 n번 실행
    temp = []
    for j in range(1, i):  # 최대 n번 실행
        temp.append(dp_list[i - j] + dp_list[j])
    dp_list[i] = max(Price_list[i], max(temp))
print(dp_list[N])
