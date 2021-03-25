import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())

    if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        if a == b == c == 0:
            break
        else:
            print("right")
            pass
    else:
        print("wrong")