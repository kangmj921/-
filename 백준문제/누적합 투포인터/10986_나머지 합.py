# 일단 모든 원소에서의 누적합을 구한 뒤,
# 해당 누적합을 하나 씩 조회하면서 딕셔너리에 저장한다.
# 그리고 누적합을 M으로 나눈 나머지가 나온 횟수 역시 딕셔너리에 저장한다.


# 누적합이 S일 때, S가 M으로 나누어 떨어진다면, 나머지 값은 0이 될 텐데,
# 이러면 아까 나머지가 나온 횟수를 저장한 딕셔너리에서 나머지 값 0이 나온 횟수만큼
# 경우의 수가 생긴다.
# 예를 들어, A_list = [1, 2, 3, 1, 2], 누적합 리스트가 [1, 3, 6, 7, 9]이고
# M이 3일 때, S5 = 9로, M으로 나누어 떨어진다.
# 하지만 S5 - S2 = A3 + A4 + A5 = 6, S5 - S3 = A4 + A5 = 3 인 경우도 있다.
# 이 경우들의 공통점은 S5에서 3으로 나누어 떨어졌던, S2, S3을 빼주었다는 것이다.
# 따라서 S5에서 얻을 수 있는 경우의 수는 3으로 나누어 떨어졌던 누적합의 개수이다.
#
# 만약 누적합이 M으로 나누어 떨어지지 않는 경우, 나머지 값은 1, 2, ..., M - 1이 된다.
# 나머지가 존재하게 되면 다른 누적합 값에서 빼서 0이 될 수 있도록 해야한다.
# 따라서 같은 나머지를 가지는 누적합 값이 있다면 해당 값과의 차이의 M으로 나눈 나머지가
# 0이 된다.
# 누적합이 M으로 나눈 몫이 1보다 크면, 부분합으로 2M으로도 만들 수 있고
# M으로도 만들 수 있다. 이 때는 나머지 값이 나온 만큼의 횟수 - 1(자기 자신 제외)을 더하고
# 그 외의 경우엔
# 해당 나머지만큼의 누적합이 나온적 있는지 확인하고 +1 한다.
#
N, M = map(int, input().split())
A_list = list(map(int, input().split()))
answer = 0
S_list = [A_list[0]]
s_dict = dict()
mod_dict = dict()
for i in range(1, N):
    S_list.append(S_list[-1] + A_list[i])
# print(S_list)
for s in S_list:
    # print(s_dict)
    s_dict[s] = 1
    temp = s % M
    if mod_dict.get(temp) is None:
        mod_dict[temp] = 1
    else:
        mod_dict[temp] += 1
    # 누적합을 M으로 나눈 나머지를 키값으로 하고
    # 그 키 값이 나온 횟수를 value로 하는 mod_dict

    if temp:  # 누적합의 M으로 나누어 떨어지지 않음.
        # 따라서 부분합이 M으로 나누어 떨어지는지 확인해야함
        if s // M > 1:  # 누적합을 M으로 나눈 몫이 1보다 크면
            # M의 배수인 부분합의 개수만큼 경우의 수 더한다.
            # 부분합의 개수는 지금까지 M으로 나눈 나머지를 키값으로 하는 값
            answer += (mod_dict[temp] - 1)
        else:
            if temp != s and s_dict.get(temp) is not None:
                answer += 1
    else:  # 누적합이 M으로 나누어 떨어짐.
        answer += (mod_dict[temp])
    # print(mod_dict, answer)
print(answer)

# 좀 더 최적화 된 풀이

# N, M = map(int, input().split())
# arr = list(map(lambda x: int(x) % M, input().split()))
#
# cnt = [0] * M
# temp = 0
# for i in range(N):
#     temp += arr[i]
#     cnt[temp % M] += 1
#
# ans = cnt[0]
# for i in cnt:
#     ans += i * (i - 1) // 2
#
# print(ans)