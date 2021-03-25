import sys
N = int(input())
word_list = list()
r = open("1181_단어 정렬_sample_input.txt", 'r')
for i in range(N):
    word_list.append(sys.stdin.readline().rstrip('\n'))
    #word_list.append(r.readline().rstrip('\n'))
set_list = list(set(word_list))
set_list.sort()
set_list.sort(key=lambda x:len(x))
for i in set_list:
    print(i)
