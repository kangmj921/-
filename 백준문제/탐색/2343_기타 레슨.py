# 1개의 레슨 영상의 길이보다 블루레이의 크기가 짧으면 안되는 경우를 생각 못했었다.
def check(S_mid):
    global answer
    # print(S_mid)
    count = 0
    total_lesson = 0
    for i in range(N - 1):
        if S_mid < lesson_list[i]:
            return False
        total_lesson += lesson_list[i]
        if total_lesson + lesson_list[i + 1] > S_mid:
            total_lesson = 0
            count += 1
        if i == N - 2 and total_lesson < S_mid:
            count += 1
    # print(count)
    if count > M:
        return False
    else:
        return True


N, M = map(int, input().split())
lesson_list = list(map(int, input().split()))
S_list = [lesson_list[0]]
for i in range(1, N):
    S_list.append(S_list[-1] + lesson_list[i])
# print(S_list)
start, end = S_list[0], S_list[-1]
# answer = 10 ** 12
while start <= end:
    mid = (start + end) // 2
    if check(mid):  # 현재 블루레이 크기로 M 개의 블루레이에 강의를 모두 담을 수 있음.
        # 최소 크기를 구해야하므로, 탐색 값 범위를 더 줄여봄.
        end = mid - 1
    else:  # 현재 블루레이 크기로 M 개의 블루레이에 강의를 모두 담을 수 없음.
        # 강의를 모두 담아야하므로, 탐색 값 범위를 더 늘려봄.
        start = mid + 1
    # print(start, end)
print(start)
