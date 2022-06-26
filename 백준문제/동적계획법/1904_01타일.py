# dp를 찾는 원리 문제의 상황에서 맨 앞에 올 수 있는 타일은 2가지 뿐이다.
# 00 타일과 1 타일.
#
# 00 타일이 올 경우 00..으로 시작
# 1 타일이 올 경우 1...로 시작.
#
# 이때 '길이가 N인 이진 수열의 개수'를 f(N)이라고 정의한다.
#
# 그러면 경우 (1)의 가짓수는 f(N-2)가 되고 경우 (2)의 가짓수는 f(N-1)이 될 것이다.
#
# 따라서 전체 경우의 수 f(N) 은 경우 (1) 과 (2)의 가짓수의 합인
#
# f(N) = f(N-1) + f(N-2)가 된다.
#
import sys


if __name__ == '__main__':
    input_num = int(sys.stdin.readline())
    dp_list = [1] * 2
    for i in range(2, input_num + 1):
        dp_list.append((dp_list[i - 1] + dp_list[i - 2]) % 15746)
    print(dp_list[input_num])
