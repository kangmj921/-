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

# 이분탐색
# 1. 입력을 받으면서 휴게소 배열의 양 끝에 출발지점과 도착지점을 추가해주고 정렬
# 2. start, end는 휴게소 위치의 범위
# 3. 이분탐색
#     - mid : 가장 멀리 떨어져 있는 휴게소 사이 거리
#     - new_store : 설치해야 할 휴게소 개수
#     - 모든 거리를 완전 탐색을 해서 mid보다 큰 경우, 해당 mid로 나누어서 설치해야 할 휴게소 개수를 구한다.
#     - 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다.
#     - 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다. (조건 만족은 했으므로 result = mid)
# 4. result 출력
N, M, L = map(int, input().split())
station_list = [0] + list(map(int, input().split())) + [L]
station_list.sort()
start = 1
end = L - 1
answer = 0
while start <= end:
    new_store = 0
    mid = (start + end) // 2
    for i in range(1, len(station_list)):
        if station_list[i] - station_list[i - 1] > mid:
            new_store += (station_list[i] - station_list[i - 1] - 1) // mid
    if new_store <= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)
