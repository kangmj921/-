import sys
sys.setrecursionlimit(10**4)


def find_final_soldier(seq, sol_list, num_of_soldier):
    if sol_list[0] == 1:
        sol_list.pop(0)
        find_final_soldier(seq, sol_list, num_of_soldier-1)
    else:
        if num_of_soldier == 2:
            print(sol_list[0], sol_list[1])
        else:
            if seq < len(sol_list):
                i = seq
                sol_list.pop(i)
            else:
                i = seq % len(sol_list)
                sol_list.pop(i)
            find_final_soldier(i + (K - 1), sol_list, num_of_soldier - 1)


if __name__ == '__main__':
    for Test_Case in range(int(sys.stdin.readline())):
        N, K = map(int, sys.stdin.readline().split())
        soldier_list = [i+1 for i in range(N)]
        find_final_soldier(K - 1, soldier_list, N)
