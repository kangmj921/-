# 처음엔 2차 리스트로 체스판을 구현해서 일일히 퀸의 위치를
# 완전탐색하려 했으나 너무 복잡해져버렸다
# 그러다 퀸의 위치를 1차 리스트로 구현한 코드를 보고 그 아이디어를 바탕으로
# 다시 구현하였다. 퀸의 위치가 [i][j]일때, 1차원 리스트에 기록되는 위치는
# chess_board[i] = j 이다.
# 체스판 기준으로 위쪽부터 퀸을 놓고 있으므로 다음 퀸을 놓을때 고려해야될 것으로는
# 같은 열에 다른 퀸이 있거나 왼쪽, 오른쪽 대각선 위에 다른 퀸이 있는 경우이다.
# 같은 열에 다른 퀸이 있는 경우는 chess_board 값이 같은 경우를 보면 되고
# 왼쪽 대각선, 오른쪽 대각선 위쪽의 경우는 규칙에 따라 정리하였다.
def check(r):
    for i in range(r):
        if chess_board[r] == chess_board[i] or abs(chess_board[r] - chess_board[i]) == abs(r - i):
            return False
    return True


def DFS(i):
    global answer
    if i == N:
        answer += 1
        return
    for j in range(N):
        chess_board[i] = j
        if check(i):
            DFS(i + 1)


for T in range(int(input())):
    N = int(input())
    answer = 0
    chess_board = [0] * N
    DFS(0)
    print("#{} {}".format(T + 1, answer))
