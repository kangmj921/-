# S -> T 로 만들 생각을 하지 않고 뒤집어서 T -> S로 만든다고 생각하면
# T에서 할일은 2가지 이다. A를 빼거나 B를 빼고 싶다면 빼고 뒤집어야함.
# 따라서 T의 맨 뒤의 문자에 따라 T에서 할 행동이 정해진다.
#
S = list(input().rstrip())
T = list(input().rstrip())
answer = False
if S == T:
    answer = True
else:
    while T:
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            for j in range(len(T) // 2):
                temp = T[len(T) - 1 - j]
                T[len(T) - 1 - j] = T[j]
                T[j] = temp
        # print(S, T)
        if S == T:
            answer = True
            break
print(1 if answer else 0)
