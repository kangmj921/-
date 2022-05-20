for T in range(int(input())):
    answer = 0
    N = int(input())
    box_list = []
    for _ in range(N):
        p, q = map(float, input().split())
        answer += p * q
    print("#{} {:.6f}".format(T + 1, answer))
