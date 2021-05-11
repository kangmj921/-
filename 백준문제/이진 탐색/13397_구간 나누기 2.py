# 배열을 M개 이하의 구간으로 나눠서 구간 점수의 최댓값을 최소로 한다.
# 배열의 길이는 최대 5,000이고 나눌 M의 크기도 마찬가지.
# 이분 탐색을 어떻게 활용할지 고민이 많이 된다.
# 전체 조건 중에 최솟값은, 배열이 최대 1개의 원소로 쪼개진 것에서
# 점수를 구하는 것. = 0
# 최댓값은, 배열이 쪼개지지 않고 1개의 구간에서 점수를 구하는 것.
# 점수를 이분탐색하면서, 해당 점수가 M개의 구간으로 divide 했을 때
# 가능한 최대 점수를 확인하고 mid보다 작으면 앞의 구간을 선택하고,
# 아닐 경우, 뒤의 구간을 탐색한다.
# 이진탐색의 경우 O(log2(10000))의 시간복잡도를 가지며, 한 번의 탐색
# 마다 divide함수의 시간복잡도만큼 걸린다. divide 함수의 최악 시간복잡도
# 가 O(n^2) 밑으로 걸릴 수 있도록 하자.
import sys


def divide_list(target):

    pass


N, M = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))
result = []
start = 0
end = max(num_list) - min(num_list)
while start <= end:
    mid = (start + end) // 2
    if divide_list(mid) < mid: start = mid + 1
    else: end = mid - 1
print(start)
