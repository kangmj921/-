for T in range(int(input())):
    N = int(input())
    deck_list = list(input().split())
    answer = ""
    A_list, B_list = deck_list[:N//2 + N % 2], deck_list[N//2 + N % 2:]
    i = 0
    while i < len(A_list) and i < len(B_list):
        answer += A_list[i] + " " + B_list[i] + " "
        i += 1
    if i < len(A_list):
        answer += A_list[-1]
    elif i < len(B_list):
        answer += B_list[-1]
    print("#{} {}".format(T + 1, answer))
