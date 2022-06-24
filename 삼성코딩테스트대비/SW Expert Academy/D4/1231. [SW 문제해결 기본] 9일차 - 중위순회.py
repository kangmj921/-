def in_order_search(start_node):
    global answer
    if not graph[start_node][0] :
        answer += input_string[start_node][1]
        return
    in_order_search(graph[start_node][0])
    answer += input_string[start_node][1]
    if len(graph[start_node]) > 1:
        in_order_search(graph[start_node][1])


for TC in range(10):
    answer = ''
    N = int(input())
    graph = [[0] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    input_string = [[]]
    for _ in range(N):
        input_string.append(list(input().split()))
    for i in range(1, N + 1):
        node_num = int(input_string[i][0])
        if node_num > 1:
            parent_node = node_num // 2
            if node_num % 2 == 0:  # node_num // 2의 왼쪽 자식
                graph[parent_node] = [node_num]
            else:  # node_num // 2의 오른쪽 자식
                graph[parent_node].append(node_num)
    in_order_search(1)
    print("#{} {}".format(TC + 1, answer))