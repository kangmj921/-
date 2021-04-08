import sys


def make_only_friend_relationship(visited, fri_relation, n):
    #cache_visited = visited[:]
    x, y = fri_relation[n]
    print(x, y, visited)
    if n == len(visited):
        return 0
    else:
        for k in range(n, len(visited)):
            if fri_relation[k].count(x) == 0 and fri_relation[k].count(y) == 0:
                if visited[k]:
                    pass
                else:
                    visited[k] = 1
                    make_only_friend_relationship(visited, fri_relation, n + 1)


for k in range(int(input())):
    friend_relationship = list()
    n, m = map(int, input().split())
    str = list(map(int, sys.stdin.readline().split()))
    for t in range(m):
        x, y = str[2*t], str[2*t+1]
        friend_relationship.append(sorted([x, y]))
    print(friend_relationship)
    visited = [0 for i in range(m)]
    make_only_friend_relationship(visited, friend_relationship, 0)
