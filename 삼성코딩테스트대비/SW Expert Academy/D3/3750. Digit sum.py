# 입력값이 여러개일때, 각 테스트 케이스에 대한 답을 매번 출력하는 것과
# 한꺼번에 출력에 시간이 많이 차이 나게 된다.
TC = []
for T in range(int(input())):
    n = input()
    while True:
        n = str(n)
        if len(n) == 1:
            TC.append(n)
            break
        else:
            digit_list = []
            for i in n:
                digit_list.append(int(i))
            n = str(sum(digit_list))
j = 1
for i in TC:
    print("#{} {}".format(j, i))
    j += 1
