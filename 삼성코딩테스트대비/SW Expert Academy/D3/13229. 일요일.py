day_dict = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 7}


for T in range(int(input())):
    S = input().rstrip()
    answer = 7 - day_dict[S]
    if not answer:
        answer = 7
    print("#{} {}".format(T + 1, answer))
