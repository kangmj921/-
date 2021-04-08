import sys
sys.setrecursionlimit(10**4)


class Node:
    def __init__(self, number, prev=None, next=None):
        self.number = number
        self.prev = prev
        self.next = next


def construct_node(n):
    n_node = Node(n, None, None)
    return n_node


def delete_node(node):
    node.prev.next = node.next
    node.next.prev = node.prev
    return node.next


def construct_linked_list(number_of_soldier):
    i = 0
    if i == 0:
        node = construct_node(i)
        root = node
        i += 1
    while i < number_of_soldier:
        new_node = construct_node(i)
        node.next = new_node
        new_node.prev = node
        node = new_node
        i += 1
    node.next = root
    root.prev = node
    return root


def find_final_soldier(seq, sol, num_of_sol):
    if sol.number == 0:
        sol = delete_node(sol)
        find_final_soldier(seq, sol, num_of_sol-1)
    else:
        if num_of_sol == 2:
            if sol.number < sol.next.number:
                print(sol.number + 1, sol.next.number + 1)
            else:
                print(sol.next.number + 1, sol.number + 1)
        else:
            i = 0
            while i < seq:
                sol = sol.next
                i += 1
            sol = delete_node(sol)
            find_final_soldier(seq, sol, num_of_sol - 1)


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        N, K = map(int, sys.stdin.readline().split())
        soldier_list = construct_linked_list(N)
        find_final_soldier(K - 1, soldier_list, N)
