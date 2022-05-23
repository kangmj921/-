# 확장된 유클리드 호제법으로 접근해야 하는 문제이다.
for T in range(int(input())):
    A, B = map(int, input().split())
    x1, y1, x2, y2 = 1, 0, 0, 1
    while B > 0:
        q = A // B
        temp = A - q * B
        A, B = B, temp
        x = x1 - q * x2
        x1, x2 = x2, x
        y = y1 - q * y2
        y1, y2 = y2, y
    x, y = x1, y1
    print("#{} {} {}".format(T + 1, x, y))
