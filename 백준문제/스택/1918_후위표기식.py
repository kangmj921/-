import sys


# 후위 표현식은 일반 문자는 출력, ')'가 나오면 스택의 pop이 '('가 나올때까지
# pop을 하고, 일반 연산자의 경우 스택에 다른 연산자가 있으면, 자신의 우선순위가
# 스택에서 제일 클 수 있도록 스택에서 연산자를 pop한다.
# 모든 과정이 끝나고 스택에 남은 연산자가 있다면, 스택이 빌 때 까지 pop을 한다.
class Stack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


def solution(s):
    opstack = Stack()
    answer = ''
    for i in s:
        if i in prec.keys():
            if i in '*+-/':
                while not opstack.isEmpty() and prec[i] <= prec[opstack.peek()]:
                    answer += opstack.pop()
            opstack.push(i)
        elif i == ')':
            b = opstack.pop()
            while b != '(':
                answer += b
                b = opstack.pop()
        else:
            answer += i
    while not opstack.isEmpty():
        answer += opstack.pop()
    return answer


a = sys.stdin.readline().rstrip('\n')
print(solution(a))
