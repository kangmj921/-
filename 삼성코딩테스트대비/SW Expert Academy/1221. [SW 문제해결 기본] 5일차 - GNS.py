from queue import PriorityQueue

for T in range(int(input())):
    answer = ""
    tc, N = input().split()
    tc, N = int(tc[1:]), int(N)
    tc_str = list(input().split())
    trans_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
                  "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    que = PriorityQueue(maxsize=N)
    for i in tc_str:
        que.put((trans_dict[i], i))
    for i in range(N):
        answer += que.get()[1] + " "
    print("#{} {}".format(tc, answer))
