def check(row):  # 해당 열에 놓을 수 있는지 체크
    for i in range(row):
        if chess_board[i] == chess_board[row] or abs(chess_board[i] - chess_board[row]) == abs(i - row):
            # 현재 열의 전 부터 탐색해서 현재 열의 몇 행에 퀸을 놓을 수 있는지 확인한다.
            # 퀸을 놓을 수 있는 조건은 같은 행이 아니거나, 대각선이 아닌 경우이다.
            # 같은 행인 경우 chess_board 리스트의 값이 같은 경우이고
            # 대각선인 경우는 열끼리의 인덱스를 뺀 값의 절댓값과 행끼리의 인덱스를 뺀 값의 절댓값이 같은 경우
            return False
    return True


def dfs(i):
    global answer
    if i == N:
        answer += 1
        return
    for j in range(N):
        chess_board[i] = j
        if check(i):
            dfs(i + 1)


answer = 0
N = int(input())
chess_board = [0] * N  # chess_board[i] = j일때, i열 j행에 퀸이 존재함을 나타냄.
dfs(0)  # 0열부터 시작해서 각 열에 1개씩 총 N개의 퀸을 놓음.
print(answer)
