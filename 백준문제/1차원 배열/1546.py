N = int(input())
grade = list(map(int, input().split()))
M = max(grade)
for k in range(len(grade)):
    grade[k] = grade[k] / M * 100
avg = sum(grade[0:len(grade)])/len(grade)
print("%.2f" % avg)
