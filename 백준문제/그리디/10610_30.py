# 자리수의 합이 3의 배수면 3의 배수이다.
# 찾는 것은 30의 배수이므로, 0이 포함되어있어야한다.
# 3의 배수가 될 수 있음이 판정되면 수를 오름차순으로 정렬한게 최대값
N = list(map(int, input()))
if 0 not in N:
    print(-1)
else:
    if sum(N) % 3:
        print(-1)
    else:
        N.sort(reverse=True)
        print("".join(map(str, N)))
