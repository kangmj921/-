# DFS와 BFS 문제라기 보단, 문제에 주어진 조건에 맞게 구현하는 문제인 것 같다.
def check_correct(p):
    stack = []
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return True


def to_correct(p):
    if p == '':
        return p
    open_, close_ = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_ += 1
        else:
            close_ += 1
        if open_ == close_:
            break
    if i + 1 == len(p):
        v = ''
    else:
        v = p[i + 1:]
    u = p[:i + 1]
    if check_correct(u):
        u += to_correct(v)
        return u
    else:
        temp = '(' + to_correct(v) + ')'
        temp2 = ''
        for i in range(len(u)):
            if i != 0 and i != len(u) - 1:
                if u[i] == ')':
                    temp2 += '('
                else:
                    temp2 += ')'
        temp += temp2
        return temp


def solution(p):
    if check_correct(p):
        return p
    answer = to_correct(p)
    return answer


p = input()
print(solution(p))