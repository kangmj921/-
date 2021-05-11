class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1
        return curr

    def insertAfter(self, prev, item):
        next = prev.next
        newNode = Node(item)
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def traverse(self, curr, index):
        for i in range(index):
            curr = curr.next
        return curr

    def traverse_all(self, target, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
            if curr.data == target - 1:
                return curr

    def reverse(self, curr, index):
        for i in range(index):
            curr = curr.prev
        return curr


def solution(n, k, cmd):
    d_list = DoubleLinkedList()
    stack = []
    answer = ''
    for i in range(n):
        curr = d_list.tail.prev
        d_list.insertAfter(curr, i)
    curr = d_list.getAt(k + 1)
    for command in cmd:
        if command[0] == 'U':
            c, N = command.split()
            curr = d_list.reverse(curr, int(N))
        elif command[0] == 'D':
            c, N = command.split()
            curr = d_list.traverse(curr, int(N))
        elif command == 'C':
            if curr.next == d_list.tail:
                stack.append(d_list.popAfter(curr.prev))
                curr = curr.prev
            else:
                stack.append(d_list.popAfter(curr.prev))
                curr = curr.next
        else:
            removed_data = stack.pop()
            print(d_list.nodeCount)
            temp = d_list.traverse_all(removed_data, d_list.nodeCount)
            d_list.insertAfter(temp, removed_data)
    answer = ["O"] * n
    for i in stack:
        answer[i] = 'X'
    return ''.join(answer)

# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))