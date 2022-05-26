T = int(input())
result = []


def search(a, b, c, d, string):
    global temp
    if temp != '':
        return
    if abs(b - c) > 1:  # 이 조건이 왜 걸러내는 조건에 만족하는지 모르겠음
        return
    if a < 0 or b < 0 or c < 0 or d < 0:
        return
    if a == 0 and b == 0 and c == 0 and d == 0:
        temp = string
        return
    if string[-1] == '0' and a == 0 and b == 0:
        return
    if string[-1] == '1' and c == 0 and d == 0:
        return
    if string[-1] == '0':
        search(a - 1, b, c, d, string + '0', )
        search(a, b - 1, c, d, string + '1', )
    elif string[-1] == '1':
        search(a, b, c - 1, d, string + '0')
        search(a, b, c, d - 1, string + '1')


for _ in range(T):
    A, B, C, D = map(int, input().split())
    # A = 00 B = 01 C = 10 D = 11
    temp = ''
    search(A, B, C, D, '0')
    if temp == "":
        search(A, B, C, D, '1')
    result.append(temp)

for i in range(T):
    print("#{} {}".format(i + 1, result[i] if result[i] != "" else "impossible"))
