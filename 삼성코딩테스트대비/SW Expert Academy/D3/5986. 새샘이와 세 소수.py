# 홀수를 세 소수의 합으로 표현하기 위해서
# 주어진 N보다 작은 수 중 소수의 목록을 먼저 찾고
# 해당 소수 목록에 3개를 무작위로 뽑았을때 합이 N인 경우를 찾자
def search_prime(n):
    if n == 2:
        prime_list.append(2)
        return
    for i in range(2, n - 1):
        if n % i == 0:
            return
    prime_list.append(n)


def search(index, n, selected_num):
    global answer
    if n == N and selected_num == 3:
        answer += 1
        return
    if selected_num > 2:
        return
    for i in range(index, len(prime_list)):
        search(i, n + prime_list[i], selected_num + 1)
    return


for T in range(int(input())):
    N = int(input())
    answer = 0
    prime_list = []
    for i in range(2, N):
        search_prime(i)
    search(0, 0, 0)
    print("#{} {}".format(T + 1, answer))
