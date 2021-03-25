import sys
C = int(input())
for k in range(C):
    result = list(sys.stdin.readline())
    score = 0
    result_score = 0
    for t in range(len(result)):
        if result[t] == 'O':
            score += 1
        else:
            score = 0
        result_score += score
    print(result_score)