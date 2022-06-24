from collections import deque


def bfs_search(start, depth):
    visit_list = [0] * (N + 1)
    temp = []
    queue = deque()
    queue.append((start, 0))
    visit_list[start] = 1
    result = 0
    while queue:
        start_node, cnt = queue.popleft()
        if depth and cnt == depth:
            temp.append(start_node)
        else:
            result = max(result, cnt)
        for next_node in range(1, len(adjacent_list[start_node])):
            if adjacent_list[start_node][next_node] and not visit_list[next_node]:
                visit_list[next_node] = 1
                queue.append((next_node, cnt + 1))
    if not depth:
        return result
    else:
        return temp


for TC in range(10):
    answer = 0
    N, start = map(int, input().split())
    adjacent_list = [[0] * (N + 1) for _ in range(N + 1)]
    input_list = list(map(int, input().split()))
    for i in range(0, len(input_list) - 1, 2):
        from_, to_ = input_list[i], input_list[i + 1]
        adjacent_list[from_][to_] = 1
    max_depth = bfs_search(start, 0)
    answer = max(bfs_search(start, max_depth))
    print("#{} {}".format(TC + 1, answer))
