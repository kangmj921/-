import sys


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
