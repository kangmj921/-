# 현재 재료를 선택할지 안할지를 2개의 DFS로 구현해서 풀어야한다.
def DFS(selected_ing, score, total_kcal):
    global answer
    if total_kcal > limit_kcal:
        return
    if selected_ing >= num_of_ing:
        if answer < score:
            answer = score
        return
    i = selected_ing
    DFS(selected_ing + 1, score + ing_list[i][0], total_kcal + ing_list[i][1])
    DFS(selected_ing + 1, score, total_kcal)


T = int(input())
for tc in range(T):
    num_of_ing, limit_kcal = map(int, input().split())
    ing_list = [list(map(int, input().split())) for i in range(num_of_ing)]
    answer = 0
    DFS(0, 0, 0)
    print("#{} {}".format(tc + 1, answer))
