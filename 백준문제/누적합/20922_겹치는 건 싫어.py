# 투 포인터를 사용해서 현재까지 기록한 수열에서 같은 수가 K개 이하이면
# 오른쪽 포인터를 계속 이동시키고, 만약 K개 보다 많아진다면,
# 왼쪽 포인터를 오른쪽 포인터와 같은 곳으로 이동시키고 새로 수열을 기록한다.
# 기록하는 건 딕셔너리를 사용하면 간단하게 구할 수 있다.
# 시간 복잡도는 최대 O(N)
N, K = map(int, input().split())
N_list = list(map(int, input().split()))
i, j = 0, 0
n_dict = dict()
answer = 0
while True:
    if j == N:
        answer = max(answer, j - i)
        break
    if n_dict.get(N_list[j]) is None:
        n_dict[N_list[j]] = 1
    else:
        if n_dict[N_list[j]] == K:
            answer = max(answer, j - i)
            n_dict[N_list[i]] -= 1
            i += 1
            continue
        else:
            n_dict[N_list[j]] += 1
    j += 1
print(answer)
