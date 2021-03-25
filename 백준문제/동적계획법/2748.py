def Pibonazzi(N):
    number_list = [0, 1, 1]
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        index = 3
        while N > index:
            N -= 1
            number_list.append(number_list[-1] + number_list[-2])
        return number_list[-1] + number_list[-2]


if __name__== '__main__':
    print(Pibonazzi(int(input())))