# 문제 풀이는 맞는거 같은데 오답이다. 반례를 찾아보아야겠다...
N = int(input())
date_list = []
for i in range(N):
    date_list.append(list(map(int, input().split())))
date_list.sort(key=lambda x: x[0])


start, end = 0, 0
# 시작일이 가장 앞선 일정부터 정렬된 것을, 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 정렬되도록 정렬함.
for i in range(len(date_list)):
    if date_list[i][0] == date_list[start][0]:
        end = i
    else:
        if (start - end) != 0:
            temp = sorted(date_list[start:end + 1], reverse=True, key=lambda x: x[1])
            date_list[start:end + 1] = temp
        start, end = i, i
temp = sorted(date_list[start:end + 1], reverse=True, key=lambda x: x[1])
date_list[start:end + 1] = temp


# 위의 정렬로 인해 일정은 시작일이 제일 빠른 순으로 정렬되고, 시작일이 같은 일정들은 끝나는 날이 내림차순으로 졍렬됨.
# 일정들을 규칙에 의거하여 채워나가고 면적 구함.
max_date = max(map(max, date_list)) + 1     # 일정의 끝나는 날이 제일 늦은 날 값 구함
visited = [[0] * max_date]  # 일정이 채워졌는지 아닌지 기록
rows = 1    # 코팅지 세로 길이
result = 0
start, end = 0, 0
for s, e in date_list:
    if start == 0 and end == 0:     # 제일 처음 일정 기록
        start, end = s, e
        visited[rows-1][start:end + 1] = [1] * (end - start + 1)
    else:
        if s <= end + 1:    # 일정이 서로 붙어있어서 한 면적에 포함될 때
            end = max(e, end)   # 서로 붙어있는 일정의 제일 늦게 끝나는 날
            for i in range(len(visited)):   # 일정 기록을 한 줄씩 검사
                if visited[i][s:e+1] != [0] * (e - s + 1) \
                        and i == len(visited) - 1:    # 제일 마지막 줄까지 일정이 차있어서 기록하지 못할 때 일정 기록 한 줄 추가
                    i += 1
                    visited.append([0] * max_date)
                    visited[-1][s:e+1] = [1] * (e - s + 1)
                elif visited[i][s:e+1] == [0] * (e - s + 1):    # 일정 기록이 빈 곳이 있을 경우 최상단의 한 줄에 대해서만 기록
                    visited[i][s:e+1] = [1] * (e - s + 1)
                    break
            rows = max(i + 1, rows)     # 코팅지의 세로 길이 최신화
        else:       # 일정이 따로 떨어지는 경우
            result += (end - start + 1) * rows      # 기존 코팅지 면적 구함
            start, end, rows = s, e, 1      # 새로 구할 코팅지 면적에 필요한 변수 초기화
            visited[rows-1][start:end+1] = [1] * (end - start + 1)      # 일정 기록
    print(result, rows, visited)
result += (end - start + 1) * rows      # 마지막 코팅지 면적 더해줌.
print(result)
