# LCS 알고리즘을 사용한 dp 로 문제를 해결하는 문제이다.
# LCS 알고리즘은, 두 문자열에서 연속적으로 이어지지는 않았지만 순서는 맞는 부분 문자열을 찾는 알고리즘이다.
# 문자열 각각의 앞에 0을 추가하고 각 위치의 값에 LCS의 길이를 초기화하는 과정을 거친다.
# 예를 들어, ACAYKP, CAPCAK가 있을때,
#   0 A C A Y K P
# 0 0 0 0 0 0 0 0
# C 0 0 1 1 1 1 1
# [C, C]의 1은 C와 AC 사이의 LCS 길이이다. 마찬가지로 [C, Y]의 1은 C와 ACAY의 LCS 길이이다.
# 따라서 같은 문자가 나오면 이전까지의 LCS 길이에 +1을 하는데,
# 두 문자열에서 해당 두 문자를 비교하기 전의 LCS 길이에 +1을 한다.
# 비교한 문자가 다르다면, 비교한 문자 이전 LCS 중에 큰 것을 선택한다.
A = input().rstrip('\n')
B = input().rstrip('\n')
dp_list = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if B[i - 1] == A[j - 1]:
            dp_list[i][j] = dp_list[i - 1][j - 1] + 1
        else:
            dp_list[i][j] = max(dp_list[i - 1][j], dp_list[i][j - 1])
print(dp_list[len(B)][len(A)])
