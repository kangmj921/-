def DFS(index, total_height, n):
    global right_list
    if total_height == 100 and n == 7:
        for j in range(len(visited)):
            if visited[j]:
                print(height_list[j])
        print(height_list[index])
        exit()
    visited[index] = 1
    for i in range(index + 1, 9):
        if not visited[i] and total_height + height_list[i] <= 100:
            DFS(i, total_height + height_list[i], n + 1)
            visited[i] = 0


height_list = []
for _ in range(9):
    height_list.append(int(input()))
height_list.sort()
for i in range(len(height_list)):
    visited = [0] * 9
    DFS(i, height_list[i], 1)
