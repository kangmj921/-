# 슬라이딩 윈도우를 사용하면 간단하게 풀 수 있는 문제

from collections import deque


S, P = map(int, input().split())
# 1 <= P, S <= 1,000,000
DNA_string = input().rstrip()
A, C, G, T = map(int, input().split())
result = DNA_string[:P]
count = dict()
count['A'] = result.count('A')
count['C'] = result.count('C')
count['G'] = result.count('G')
count['T'] = result.count('T')
start, end = 0, P - 1
answer = 0
result = deque(result)
while True:
    if count['A'] >= A and count['C'] >= C and count['G'] >= G and count['T'] >= T:
        # print(result, count)
        answer += 1
    to_sub = result.popleft()
    start += 1
    end += 1
    if end == S:
        break
    to_add = DNA_string[end]
    result.append(to_add)
    count[to_sub] -= 1
    count[to_add] += 1
print(answer)
