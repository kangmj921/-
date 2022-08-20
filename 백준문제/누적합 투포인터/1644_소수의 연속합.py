# 에라토스테네의 체를 이용하여 소수를 모두 구해놓은 뒤,
# N보다 작은 소수 리스트에서 연속합을 구한다
# 연속합이 N보다 작으면 뒤 부분 포인터의 위치를 오른쪽으로 이동시키고
# 크다면 왼쪽의 포인터를 오른쪽으로 이동시키면서
# 두 포인터 사이의 연속합이 N인 경우를 센다.
# N이 되어도 왼쪽 포인터는 이동 시켜줘야한다.
N_list = [False, False] + [True] * 4000000
prime_list = []
for i in range(2, 4000000 + 1):
    if N_list[i]:
        prime_list.append(i)
        for j in range(2 * i, 4000000 + 1, i):
            N_list[j] = False
# print(prime_list)
N = int(input())
answer, i, j, result = 0, 0, 0, prime_list[0]
for end in range(len(prime_list)):
    if prime_list[end] > N:
        end -= 1
        break
while True:
    if i > j:
        break
    if result < N and j < end:
        j += 1
        result += prime_list[j]
    else:
        if result == N:
            answer += 1
        result -= prime_list[i]
        i += 1
    # print(i, j, result)
print(answer)
