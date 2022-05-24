for T in range(int(input())):
    answer = []
    heap_list = [0]
    for N in range(1, int(input()) + 1):
        command = input()
        if command[0] == '1':  # 삽입 연산
            c, x = map(int, command.split())
            heap_list.append(x)
            node_num = len(heap_list) - 1
            Depth = 1
            while node_num > 1 and heap_list[node_num] > heap_list[node_num // 2]:
                temp = node_num // 2  # 현재 노드 번호의 부모 번호
                heap_list[temp], heap_list[node_num] = heap_list[node_num], heap_list[temp]  # 자식 노드가 부모 보다 크면 바꿔줌.
                node_num = temp
        else:  # 삭제 연산
            if len(heap_list) > 1:
                answer.append(heap_list[1])
                node_num = 1
                heap_list[1], heap_list[-1] = heap_list[-1], heap_list[1]
                heap_list.pop()
                while True:
                    temp = node_num * 2  # 현재 노드 번호의 자식 번호
                    if temp + 1 < len(heap_list) and heap_list[temp] < heap_list[temp + 1]:  # 만약 자식이 2개고 오른쪽이 왼쪽 보다 클 때
                        temp += 1
                    if temp >= len(heap_list) or heap_list[temp] < heap_list[node_num]:  # 부모 노드가 자식 보다 크다면 루프를 반복할 필요가 없다
                        break
                    heap_list[node_num], heap_list[temp] = heap_list[temp], heap_list[node_num]
                    node_num = temp
            else:
                answer.append(-1)
    print("#{}".format(T + 1), *answer)
