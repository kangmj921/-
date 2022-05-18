for T in range(int(input())):
    answer = 0
    target_bit = input().rstrip('\n')
    initial_bit = '0'
    for i in range(len(target_bit)):
        if target_bit[i] != initial_bit:
            initial_bit = target_bit[i]
            answer += 1
    print("#{} {}".format(T + 1, answer))
