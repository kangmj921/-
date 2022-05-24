for T in range(int(input())):
    ship_list = []
    for N in range(int(input())):
        day = int(input())
        if day != 1:
            if len(ship_list) == 0:
                ship_list.append(day - 1)
            else:
                check = False
                for i in ship_list:
                    if (day - 1) % i == 0:
                        check = True
                        break
                if not check:
                    ship_list.append(day - 1)
    print("#{} {}".format(T + 1, len(ship_list)))
