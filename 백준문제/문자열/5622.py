dial_info = {'': 1, 'ABC': 2, 'DEF': 3, 'GHI': 4,
             'JKL': 5, 'MNO': 6, 'PQRS': 7, 'TUV': 8, 'WXYZ': 9}
dial_keys = list(dial_info.keys())
time_data = dict()
initial_time = 2
total_time = 0
for dial_num in range(1, 10):
    time_data[dial_num] = initial_time
    initial_time += 1
Word = list(input())
for k in range(len(Word)):
    for t in range(len(dial_keys)):
        if dial_keys[t].find(Word[k]) >= 0:
            total_time += time_data[dial_info[dial_keys[t]]]
print(total_time)
