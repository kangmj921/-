# 슬라이딩 윈도우를 사용하는 문제
# 일정 길이의 K를 가지는 윈도우를 이동시키면서 최대 값을 찾고 이 최대 값이
# 몇 번 나왔는지 확인한다.
N, X = map(int, input().split())
N_list = list(map(int, input().split()))

S_list = [N_list[0]]
answer = 0
n_dict = dict()
for i in range(1, N):
    S_list.append(S_list[-1] + N_list[i])
i, j = 0, X - 1
while True:
    # print(i, j)
    if j == N:
        break
    result = S_list[j] - S_list[i] + N_list[i]
    if n_dict.get(result) is None:
        n_dict[result] = 1
    else:
        n_dict[result] += 1
    answer = max(answer, result)
    i += 1
    j += 1
if not answer:
    print("SAD")
else:
    print(answer)
    print(n_dict[answer])