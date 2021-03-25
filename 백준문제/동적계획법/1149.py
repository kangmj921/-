import sys


def sub_min_second_min(num_list):
    max__ = max(num_list)
    min__ = min(num_list)
    return sum(num_list) - (max__ + 2*min__), min__


def paint_house(price_list, k):
    if k + 1 < len(price_list):
        ret1, min1__ = sub_min_second_min(price_list[k])
        ret2, min2__ = sub_min_second_min(price_list[k + 1])
        if ret1 < ret2:
            stack.append(ret1 + min1__)
        else:
            stack.append(min1__)
        print(stack)
        paint_house(price_list, k + 1)
    else:
        stack.append(min(price_list[k]))
        print(stack)
        print(sum(stack))


if __name__ == "__main__":
    num_house = int(input())
    price = [list(map(int, sys.stdin.readline().split())) for k in range(num_house)]
    stack = list()
    paint_house(price, 0)
