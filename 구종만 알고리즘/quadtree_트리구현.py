import sys
import copy


class Node:
    def __init__(self, data, left1=None, left2=None, right1=None, right2=None):
        self.data = data
        self.left1 = left1
        self.left2 = left2
        self.right1 = right1
        self.right2 = right2


def construct_root(str):
    new_node = Node(str[0], None, None, None, None)
    return new_node


def construct_quad_tree(str, i, parent):
    global n
    i = n
    if i < len(str):
        if i == 0:
            new_node = copy.deepcopy(parent)
            n += 1
        else:
            new_node = Node(str[i], None, None, None, None)
            n += 1
        if str[i] == 'x':
            parent.left1 = copy.copy(construct_quad_tree(str, n, new_node))
            parent.left2 = copy.copy(construct_quad_tree(str, n, new_node))
            parent.right1 = copy.copy(construct_quad_tree(str, n, new_node))
            parent.right2 = copy.copy(construct_quad_tree(str, n, new_node))
            return parent
        else:
            return new_node
    else:
        return


def reverse_traverse(node):
    if node is None: return
    print(node.data, end='')
    reverse_traverse(node.right1)
    reverse_traverse(node.right2)
    reverse_traverse(node.left1)
    reverse_traverse(node.left2)


for recur in range(int(input())):
    n = 0
    quad_tree = sys.stdin.readline()
    root = construct_root(quad_tree)
    construct_quad_tree(quad_tree, 0, root)
    reverse_traverse(root)
    print()
