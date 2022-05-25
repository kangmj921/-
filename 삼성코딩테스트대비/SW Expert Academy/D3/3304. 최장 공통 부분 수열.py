# dp를 이용해서 푸는 문제로, LCS라는 이름으로 따로 불린다.
# LCS 알고리즘에 대해 잘 공부해보자
for T in range(int(input())):
    s1, s2 = input().split()
    dp_list = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

    for i in range(1, len(dp_list)):
        for j in range(1, len(dp_list[i])):
            if s1[j - 1] != s2[i - 1]:
                dp_list[i][j] = max(dp_list[i - 1][j], dp_list[i][j - 1])
            else:
                dp_list[i][j] = dp_list[i - 1][j - 1] + 1
    print("#{} {}".format(T + 1, dp_list[-1][-1]))
