# to_find를 구하는 부분을 abs()로 씌웠었는데, 이걸 제거하니 풀렸다.
# X보다 큰 수가 주어지는 경우. 예를 들어 abs(17 - 23)일 경우
# 6이 배열에 있으면 답이 +1 되므로 그렇다
# abs()를 너무 생각없이 넣은 것 같다.
n = int(input())
a_list = list(map(int, input().split()))
x = int(input())
n_dict = dict()
answer = 0
for i in range(n):
    n_dict[a_list[i]] = 1
for i in range(n):
    n_dict.pop(a_list[i])
    to_find = x - a_list[i]
    if n_dict.get(to_find) is not None:
        answer += 1
print(answer)
