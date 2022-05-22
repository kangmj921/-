for TC in range(int(input())):
    N, M = map(int, input().split())
    M_by_bit = str(bin(M))[2:]
    answer = "ON"
    # print(M_by_bit)
    if N > len(M_by_bit):
        answer = 'OFF'
    else:
        for i in range(len(M_by_bit) - N, len(M_by_bit)):
            if M_by_bit[i] == '0':
                answer = "OFF"
    print("#{} {}".format(TC + 1, answer))
