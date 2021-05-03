# 계수 정렬을 이용해서 쉽게 풀 수 있는 문제였다.
# 계수 정렬의 경우 데이터의 크기 범위가 제한되어 있고
# 정수 형태의 데이터일 때 사용할 수 있으며, 시간복잡도가
# 최대 O(N + K)로 빠르게 정렬할 수 있다.
import sys

count_list = [0] * 10001
for _ in range(int(input())):
    num = int(sys.stdin.readline())
    count_list[num] += 1
for i in range(len(count_list)):
    while count_list[i] > 0:
        print(i)
        count_list[i] -= 1
