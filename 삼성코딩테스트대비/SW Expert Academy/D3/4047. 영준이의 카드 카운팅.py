def solution(char, num):
    if char == 'S':
        if not S[num]:
            S[num] = 1
            return True
    if char == 'D':
        if not D[num]:
            D[num] = 1
            return True
    if char == 'H':
        if not H[num]:
            H[num] = 1
            return True
    if char == 'C':
        if not C[num]:
            C[num] = 1
            return True
    return False


for T in range(int(input())):
    check = True
    card_list = input()
    S, D, H, C = [0] * 13, [0] * 13, [0] * 13, [0] * 13
    for i in range(0, len(card_list), 3):
        index = int(card_list[i + 1] + card_list[i + 2]) - 1
        if not solution(card_list[i], index):
            print("#{} {}".format(T + 1, "ERROR"))
            check = False
    if check:
        print("#{} {} {} {} {}".format(T + 1, S.count(0), D.count(0), H.count(0), C.count(0)))
