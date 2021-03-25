import sys

N = int(input())
member = list()
for i in range(N):
    age, name = sys.stdin.readline().split()
    member.append([int(age), name])
member = sorted(member, key = lambda x:x[0])
for i in member:
    print(i[0], i[1])
