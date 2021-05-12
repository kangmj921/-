# 이분 탐색으로 어떻게 접근해야 될지 고민이 많이 되는 문제
# 휴게소가 없는 구간의 최댓값을 구하려면, 이미 설치된 휴게소
# 구간 중 가장 큰 구간이 적게 나눠질 수 있도록 휴게소를 설치하면
# 될 것이다. 일정한 구간마다 새 휴게소를 설치한다고 하였을 때,
# 최소 설치 간격 1, 최대 설치 간격 L - 1로 놓고 이분탐색을 진행한다.
# 이미 설치된 휴게소 사이의 구간을 mid로 나눈 몫이 새 휴게소를
# 설치할 수 있는 수 이며, 만약 딱 나누어 떨어지면, 이미 설치된 곳에
# 설치하게 되므로 1개 를 뺀다.
# 총 구하게 되는 설치하는 휴게소의 수가 M보다 작거나 같다면
# 최댓값의 최솟값을 구할 수 있도록, 이진탐색의 구간을
# 줄이고, 만약 그 간격이 커서 M개를 설치하지 못한다면,
# 탐색 구간을 늘리는 식으로 탐색할 것이다.
N, M, L = map(int, input().split())
station_list = list(map(int, input().split()))
station_list.sort()
width = [L - station_list[-1], station_list[0]]
for i in range(1, N):
    width.append(station_list[i] - station_list[i - 1])
width.sort()
print(width)
start = 1
end = L - 1
while start <= end:
    new_store = 0
    mid = (start + end) // 2
    for i in width:
        new_store += i // mid
        if i % mid == 0:
            new_store -= 1
    if new_store <= M:
        end = mid - 1
    else:
        start = mid + 1
print(start)
