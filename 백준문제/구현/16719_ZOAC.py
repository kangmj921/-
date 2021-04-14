# 문제의 조건을 잘못 이해함... 한 문자씩 사전순으로 보여주는줄 알았으나
# 문자열이 사전순으로 되게 하는 거였음..
# 처음에 가장 빠른 알파벳 하나 뽑고, 그 알파벳의 문자열 위치 기준 오른쪽 부터
# 사전 순으로 제일 빠른 알파벳 하나를 오른쪽에 추가함, 추가하고 나면 기준을 추가한 문자로
# 바꾸고 위의 과정을 다시 반복함. 만약 문장의 끝에 가도 추가한 문자가 없다면,
# 왼쪽으로 탐색을 시작해서 제일 빠른 문자 추가할 문자 찾음. 왼쪽이 오른쪽 보다 크게 되면 return
# 이미 찾았던 문자 다시 안 찾도록 visited 리스트 이용.
# 문자를 추가하고 나면, index대로 정렬해서 출력
def solution(left, right):
    global result
    if left > right:
        return
    idx = 'Z'
    for i in range(left, right + 1):
        if visited[i] == 0:
            idx = min(idx, c[i])
    mid = c[left:right+1].index(idx) + left
    visited[mid] = 1
    result.append(mid)
    result.sort()
    for i in range(len(result)):
        print(c[result[i]], end="")
    print('')
    solution(mid + 1, right)
    solution(left, mid - 1)


c = list(input().rstrip('\n'))
alphabet_list = []
visited = [0] * len(c)
result = []
for i in range(ord('A'), ord('Z') + 1):
    alphabet_list.append(chr(i))
solution(0, len(c) - 1)
