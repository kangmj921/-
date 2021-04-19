# DFS나 BFS로 모든 경우의 수를 찾는 식으로 접근하면 될 것 같은데
# 코딩으로 구현이 잘 안됨...
def DFS(list_, index_, p):
    print(p, list_.count(0))
    p += str(index_)
    list_[index_] -= 1
    for i in range(len(list_)):
        if list_[i] > 0:
            DFS(list_, i, p)
    if list_.count(0) == 4:
        return p


N = int(input())
A_list = list(map(int, input().split()))
letter_list = list(map(int, input().split()))
for i in range(len(letter_list)):
    if letter_list[i] != 0:
        print(DFS(letter_list, i, ''))

